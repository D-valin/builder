import React, { createContext, useContext, useState, useEffect } from 'react';
import { authApi } from '../services/api';

const AuthContext = createContext();

export const useAuth = () => {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context;
};

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    // Fetch real profile from /api/users/me
    const fetchProfile = async () => {
        try {
            const data = await authApi.getMe();
            setUser({
                username: data.username,
                full_name: data.full_name || data.username,
                email: data.email,
                role: data.role || 'CAJERO', // ADMIN, SUPERVISOR, CAJERO
            });
        } catch (error) {
            console.error('Failed to fetch profile:', error);
            // Token is invalid/expired — clear it
            localStorage.removeItem('token');
            setUser(null);
        }
    };

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (token) {
            fetchProfile().finally(() => setLoading(false));
        } else {
            setLoading(false);
        }
    }, []);

    const login = async (username, password) => {
        try {
            const data = await authApi.login(username, password);
            localStorage.setItem('token', data.access_token);
            // Fetch real user profile after login
            await fetchProfile();
            return true;
        } catch (error) {
            console.error('Login failed:', error);
            throw error;
        }
    };

    const logout = () => {
        localStorage.removeItem('token');
        setUser(null);
    };

    // Helper to check if user has required role(s)
    const hasRole = (allowedRoles) => {
        if (!user) return false;
        if (user.role === 'ADMIN') return true; // Admin has skip-all
        return allowedRoles.includes(user.role);
    };

    return (
        <AuthContext.Provider value={{
            user,
            login,
            logout,
            isAuthenticated: !!user,
            loading,
            hasRole,
            isAdmin: user?.role === 'ADMIN',
            isSupervisor: user?.role === 'SUPERVISOR',
            isCajero: user?.role === 'CAJERO'
        }}>
            {children}
        </AuthContext.Provider>
    );
};
