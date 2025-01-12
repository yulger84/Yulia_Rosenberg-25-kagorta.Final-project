SELECT 
    c.login AS courier_login, 
    COUNT(o.id) AS orders_in_delivery
FROM 
    "Couriers" c
LEFT JOIN 
    "Orders" o
ON 
    c.id = o."courierId" AND o."inDelivery" = true
GROUP BY 
    c.login
ORDER BY 
    orders_in_delivery DESC;