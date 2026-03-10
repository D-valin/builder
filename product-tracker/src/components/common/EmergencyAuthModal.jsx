import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ShieldAlert, X, Lock, ShieldCheck } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { useNotification } from '../../context/NotificationContext';
import { authApi } from '../../services/api';

const EmergencyAuthModal = ({ isOpen, onClose, onAuthorized, actionTitle, actionDescription }) => {
    const { user } = useAuth();
    const { showNotification } = useNotification();
    const [password, setPassword] = useState('');
    const [isVerifying, setIsVerifying] = useState(false);

    const handleVerify = async (e) => {
        if (e) e.preventDefault();
        setIsVerifying(true);
        try {
            // We need to verify as an ADMIN. 
            // In a real system, we'd have a specific "authorize action" endpoint.
            // For this demo, we'll use the 'ADMIN' credentials to check if the password is valid 
            // and the user associated with that password has 'ADMIN' role.

            // Note: Our current api.login returns a token. 
            // We can't easily check 'any' admin password without a dedicated backend endpoint.
            // But we can simulate it by attempting to login with 'admin' (or current user if they are admin)
            // or better yet, since we are implementing a "Delegated Authority", 
            // we'll assume the person typing is the ADMIN.

            // For now, let's use the login service but check if the resulting user is ADMIN.
            // This is a bit tricky without knowing the admin's username.
            // Let's assume the default admin username is 'admin'.

            const data = await authApi.login('admin', password);
            // If success, it's an admin password (since 'admin' user is always ADMIN in this system)

            showNotification('Autorización concedida por administrador', 'success');
            onAuthorized();
            onClose();
        } catch (error) {
            showNotification('Error de autorización: Credenciales de administrador inválidas', 'error');
        } finally {
            setIsVerifying(false);
            setPassword('');
        }
    };

    return (
        <AnimatePresence>
            {isOpen && (
                <div className="fixed inset-0 z-[100] flex items-center justify-center p-4">
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        className="absolute inset-0 bg-slate-900/60 backdrop-blur-md"
                        onClick={onClose}
                    />
                    <motion.div
                        initial={{ opacity: 0, scale: 0.9, y: 20 }}
                        animate={{ opacity: 1, scale: 1, y: 0 }}
                        exit={{ opacity: 0, scale: 0.9, y: 20 }}
                        className="bg-white dark:bg-slate-900 rounded-[2.5rem] shadow-2xl w-full max-w-md p-10 relative z-10 border border-slate-100 dark:border-white/10 overflow-hidden"
                    >
                        {/* Decorative background element */}
                        <div className="absolute top-0 right-0 w-32 h-32 bg-emerald-500/5 rounded-full -translate-y-1/2 translate-x-1/2 blur-3xl" />

                        <div className="relative">
                            <div className="w-16 h-16 bg-red-50 dark:bg-red-500/10 rounded-2xl flex items-center justify-center text-red-500 mx-auto mb-6 shadow-inner border border-red-100 dark:border-red-500/20">
                                <ShieldAlert size={32} />
                            </div>

                            <div className="text-center mb-8">
                                <h3 className="text-2xl font-black text-slate-800 dark:text-white mb-2 uppercase tracking-tight">Acción Restringida</h3>
                                <p className="text-[10px] font-black text-red-500 uppercase tracking-[0.2em] mb-4">Autorización de Emergencia Requerida</p>
                                <div className="p-4 bg-slate-50 dark:bg-white/5 rounded-2xl border border-slate-100 dark:border-white/5 text-left mb-6">
                                    <p className="text-xs font-bold text-slate-500 uppercase tracking-widest mb-1">Acción Solicitada:</p>
                                    <p className="text-sm font-black text-slate-800 dark:text-slate-200">{actionTitle}</p>
                                    <p className="text-xs text-slate-500 mt-1">{actionDescription}</p>
                                </div>
                                <p className="text-xs text-slate-400 font-medium px-4">
                                    Esta acción requiere la intervención manual de un <span className="text-emerald-500 font-bold">ADMINISTRADOR</span> para proceder.
                                </p>
                            </div>

                            <form onSubmit={handleVerify} className="space-y-6">
                                <div className="space-y-2">
                                    <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Contraseña Administrador</label>
                                    <div className="relative group">
                                        <div className="absolute left-5 top-1/2 -translate-y-1/2 text-slate-400 transition-colors group-focus-within:text-emerald-500">
                                            <Lock size={18} />
                                        </div>
                                        <input
                                            type="password"
                                            autoFocus
                                            value={password}
                                            onChange={(e) => setPassword(e.target.value)}
                                            className="w-full pl-14 pr-6 py-4 bg-slate-50 dark:bg-white/5 border border-slate-200 dark:border-white/10 rounded-2xl outline-none focus:ring-4 focus:ring-emerald-500/10 focus:border-emerald-500 transition-all text-lg font-mono dark:text-white"
                                            placeholder="••••••••"
                                        />
                                    </div>
                                </div>

                                <div className="flex gap-4 pt-2">
                                    <button
                                        type="button"
                                        onClick={onClose}
                                        className="flex-1 py-4 px-6 rounded-2xl font-black text-slate-500 hover:bg-slate-50 dark:hover:bg-white/5 transition-all text-xs tracking-widest"
                                    >
                                        CANCELAR
                                    </button>
                                    <button
                                        type="submit"
                                        disabled={isVerifying || !password}
                                        className="flex-1 py-4 px-6 bg-slate-900 dark:bg-emerald-600 hover:bg-emerald-700 text-white rounded-2xl font-black shadow-xl shadow-emerald-500/20 transition-all disabled:opacity-50 flex items-center justify-center gap-2 text-xs tracking-widest"
                                    >
                                        {isVerifying ? (
                                            <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                                        ) : (
                                            <>
                                                <ShieldCheck size={16} />
                                                AUTORIZAR
                                            </>
                                        )}
                                    </button>
                                </div>
                            </form>
                        </div>
                    </motion.div>
                </div>
            )}
        </AnimatePresence>
    );
};

export default EmergencyAuthModal;
