-- SQL Query: Superstore Sales and Orders Analysis by Product Category & Sub-Category
SELECT 
    category,
    sub_category,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(AVG(sales), 2) AS average_sale_value
FROM 
    orders
GROUP BY 
    category, 
    sub_category
ORDER BY 
    category ASC, 
    total_sales DESC;
