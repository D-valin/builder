from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import StockMovement as StockMovementModel, Product, User
from ..schemas.stock_movement import StockMovement, StockMovementCreate
from .deps import get_current_active_user

router = APIRouter()

@router.post("/", response_model=StockMovement)
def create_stock_movement(
    *,
    db: Session = Depends(get_db),
    movement_in: StockMovementCreate,
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    Record a stock movement and update product stock (RF09, RF10, RF11)
    """
    product = db.query(Product).filter(Product.id == movement_in.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Normalizar tipo a MAYUSCULAS
    m_type = movement_in.type.upper()

    # Validar que no haya stock negativo en salidas
    if m_type in ['EXIT', 'SALE'] and product.stock < movement_in.quantity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Stock insuficiente. Disponible: {product.stock}"
        )

    # Actualizar stock del producto (RF11)
    if m_type in ['ENTRY', 'RETURN']:
        product.stock += movement_in.quantity
    else:
        product.stock -= movement_in.quantity

    # Forzar que el tipo guardado sea el normalizado
    db_obj = StockMovementModel(
        **movement_in.dict(exclude={'type'}),
        type=m_type,
        user_id=current_user.id
    )
    db.add(product) # Asegurar que el cambio en producto se persiste
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    
    # Podriamos disparar alertas aqui (RF17) si product.stock <= product.min_stock
    
    return db_obj

@router.get("/", response_model=List[StockMovement])
def get_all_stock_movements(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    Get movement history for all products (unified inventory timeline)
    """
    movements = db.query(StockMovementModel)\
        .order_by(StockMovementModel.created_at.desc())\
        .offset(skip).limit(limit).all()
    return movements

@router.get("/{product_id}", response_model=List[StockMovement])
def read_stock_movements(
    product_id: int,
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    Get movement history for a specific product (RF12)
    """
    movements = db.query(StockMovementModel)\
        .filter(StockMovementModel.product_id == product_id)\
        .order_by(StockMovementModel.created_at.desc())\
        .offset(skip).limit(limit).all()
    return movements
