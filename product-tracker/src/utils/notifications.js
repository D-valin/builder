// Notification Utility
// Handles browser notifications for low stock and other alerts

export const requestNotificationPermission = async () => {
    if (!('Notification' in window)) {
        console.warn('This browser does not support notifications');
        return false;
    }

    if (Notification.permission === 'granted') {
        return true;
    }

    if (Notification.permission !== 'denied') {
        const permission = await Notification.requestPermission();
        return permission === 'granted';
    }

    return false;
};

export const showNotification = (title, options = {}) => {
    if (Notification.permission === 'granted') {
        new Notification(title, {
            icon: '/logo.png',
            badge: '/badge.png',
            ...options
        });
    }
};

export const showLowStockNotification = (product) => {
    showNotification('⚠️ Stock Bajo', {
        body: `${product.name} tiene solo ${product.stock} ${product.unit} disponibles (Mínimo: ${product.min_stock})`,
        tag: `low-stock-${product.id}`,
        requireInteraction: true
    });
};

export const showExpirationNotification = (product) => {
    showNotification('📅 Producto por Vencer', {
        body: `${product.name} vence el ${product.expiration_date}`,
        tag: `expiring-${product.id}`,
        requireInteraction: true
    });
};
