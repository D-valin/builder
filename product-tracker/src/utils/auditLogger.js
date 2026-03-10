// Audit Logger Utility
// Tracks all changes to entities with timestamp, user, and before/after values

export const createAuditLog = (entity, entityId, action, changes, user = 'Admin User') => {
    return {
        id: Date.now() + Math.random(), // Unique ID
        timestamp: new Date().toISOString(),
        user,
        entity, // 'product', 'supplier', 'purchase_order', etc.
        entityId,
        action, // 'create', 'update', 'delete', 'archive'
        changes, // { field: { old: value, new: value } }
    };
};

export const formatAuditLog = (log) => {
    const date = new Date(log.timestamp);
    const timeStr = date.toLocaleString('es-ES', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });

    let message = '';
    switch (log.action) {
        case 'create':
            message = `creó ${log.entity}`;
            break;
        case 'update':
            message = `actualizó ${log.entity}`;
            break;
        case 'delete':
            message = `eliminó ${log.entity}`;
            break;
        case 'archive':
            message = `archivó ${log.entity}`;
            break;
        default:
            message = `${log.action} ${log.entity}`;
    }

    return {
        ...log,
        formattedTime: timeStr,
        formattedMessage: message
    };
};
