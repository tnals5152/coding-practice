SELECT Customers.name as Customers
FROM Customers left join Orders
ON Customers.id = Orders.customerId
WHERE Orders.id is null
