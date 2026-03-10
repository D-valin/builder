@router.post("/password-recovery")
def recover_password(request: PasswordResetRequest, db: Session = Depends(get_db)) -> Any:
    """
    Password recovery endpoint - DIAGNOSTIC MODE
    """
    print(f"--- [DIAGNOSTIC] Password Recovery Request for: {request.email} ---")
    
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        print(f"[ERROR] User not found: {request.email}")
        raise HTTPException(
            status_code=404,
            detail="The user with this email does not exist.",
        )

    # DIAGNOSTIC HARDCODE: Return success immediately
    print(f"[SUCCESS] User found: {user.username}. Returning hardcoded success.")
    return {
        "status": "success", 
        "message": "Simulated OK - Backend logic is execution", 
        "debug_user": user.username
    }
