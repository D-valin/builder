/**
 * Formats a number as Colombian Pesos (COP)
 * Example: 338000 -> $338.000
 * @param {number} value 
 * @returns {string}
 */
export const formatCOP = (value) => {
    if (value === undefined || value === null) return '$0';

    const formatted = new Intl.NumberFormat('es-CO', {
        style: 'decimal',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(value);

    return `$${formatted}`;
};

/**
 * Alternative simple formatter if Intl has issues with specific environments
 */
export const formatCurrency = (value) => {
    if (value === undefined || value === null) return '$0';
    const formatted = Math.floor(value)
        .toString()
        .replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    return `$${formatted}`;
};
