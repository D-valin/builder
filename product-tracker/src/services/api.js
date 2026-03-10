import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

const api = axios.create({
    baseURL: API_URL,
});

// Add a request interceptor to include the JWT token
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

// Add a response interceptor to handle errors (like 401 Unauthorized or 403 Forbidden)
api.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response && (error.response.status === 401 || error.response.status === 403)) {
            localStorage.removeItem('token');
            // Only redirect if NOT on the login page to avoid infinite loops or hangs during login attempts
            if (window.location.pathname !== '/login') {
                window.location.href = '/login';
            }
        }
        return Promise.reject(error);
    }
);

export const authApi = {
    login: async (username, password) => {
        const params = new URLSearchParams();
        params.append('username', username);
        params.append('password', password);

        const response = await api.post('auth/login/access-token', params, {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        });
        return response.data;
    },
    getMe: async () => {
        const response = await api.get('users/me');
        return response.data;
    }
};

export const productsApi = {
    getAll: (params) => api.get('products/', { params }),
    getById: (id) => api.get(`products/${id}`),
    create: (data) => api.post('products/', data),
    update: (id, data) => api.put(`products/${id}`, data),
    delete: (id) => api.delete(`products/${id}`),
    archive: (id) => api.patch(`products/${id}/archive`),
    getLowStock: () => api.get('products/alerts/low-stock'),
    getExpiring: () => api.get('products/alerts/expiring'),
};

export const reportsApi = {
    getValuation: () => api.get('reports/valuation'),
    getSalesSummary: () => api.get('reports/sales-summary'),
    getTopProducts: () => api.get('reports/top-products'),
    getAlerts: () => api.get('reports/alerts'),
};

export const suppliersApi = {
    getAll: () => api.get('suppliers/'),
    create: (data) => api.post('suppliers/', data),
    update: (id, data) => api.put(`suppliers/${id}`, data),
    delete: (id) => api.delete(`suppliers/${id}`),

    // Catalogue Management
    getCatalogue: (id) => api.get(`suppliers/${id}/catalogue`),
    addToCatalogue: (id, item) => api.post(`suppliers/${id}/catalogue`, item),
    removeFromCatalogue: (id, productId) => api.delete(`suppliers/${id}/catalogue/${productId}`),
};

export const salesApi = {
    getAll: () => api.get('sales/'),
    create: (data) => api.post('sales/', data),
};

export const stockApi = {
    getAll: (params) => api.get('stock-movements/', { params }),
    getByProductId: (productId) => api.get(`stock-movements/${productId}`),
    createMovement: (data) => api.post('stock-movements/', data),
};

export const purchaseOrdersApi = {
    getAll: (params) => api.get('purchase-orders/', { params }),
    create: (data) => api.post('purchase-orders/', data),
    receive: (id, data) => api.patch(`purchase-orders/${id}/receive`, data),
    togglePayment: (id) => api.patch(`purchase-orders/${id}/toggle-payment`),
    delete: (id) => api.delete(`purchase-orders/${id}`),
};

export const auditLogsApi = {
    getAll: () => api.get('audit-logs/'),
    getByEntity: (entity, entityId) => api.get('audit-logs/', { params: { entity, entity_id: entityId } }),
};

export const clientsApi = {
    getAll: () => api.get('clients/'),
    getById: (id) => api.get(`clients/${id}`),
    create: (data) => api.post('clients/', data),
    update: (id, data) => api.put(`clients/${id}`, data),
    delete: (id) => api.delete(`clients/${id}`),
};

export const returnsApi = {
    getAll: () => api.get('returns/'),
    create: (data) => api.post('returns/', data),
};

export default api;
