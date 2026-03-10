import React from 'react';
import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';
import Header from './Header';

const MainLayout = () => {
    return (
        <div className="min-h-screen bg-transparent flex">
            <Sidebar />
            <div className="flex-1 flex flex-col md:ml-20 transition-all duration-300">
                <Header />
                <main className="flex-1 p-6 mt-16 overflow-y-auto">
                    <Outlet />
                </main>
            </div>
        </div>
    );
};

export default MainLayout;
