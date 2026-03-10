/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            fontFamily: {
                sans: ['Inter', 'system-ui', 'sans-serif'],
                display: ['Plus Jakarta Sans', 'system-ui', 'sans-serif'],
            },
            colors: {
                primary: {
                    DEFAULT: '#6366f1', // Indigo 500
                    hover: '#4f46e5',   // Indigo 600
                    light: '#e0e7ff',   // Indigo 100
                    glass: 'rgba(99, 102, 241, 0.1)',
                },
                secondary: {
                    DEFAULT: '#8b5cf6', // Violet 500
                    hover: '#7c3aed',   // Violet 600
                    light: '#ede9fe',   // Violet 100
                },
                slate: {
                    850: '#1e293b', // Custom dark for text
                },
                background: '#f0f4ff', // Light Indigo-ish background
            },
            boxShadow: {
                'glass': '0 8px 32px 0 rgba(31, 38, 135, 0.07)',
                'soft': '0 10px 40px -10px rgba(0,0,0,0.08)',
                'inner-light': 'inset 0 2px 4px 0 rgba(255, 255, 255, 0.5)',
            },
            backdropBlur: {
                'xs': '2px',
            }
        },
    },
    plugins: [],
}
