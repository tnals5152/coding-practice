# Write your MySQL query statement below
# SELECT s.stock_name as stock_name, SUM(s.p) as capital_gain_loss
# FROM (
#     SELECT stock_name, 
#         SUM(CASE WHEN operation = 'Buy' THEN price * (-1)
#              ELSE price
#         END) AS p
#     FROM Stocks) as s
# GROUP BY s.stock_name
# ORDER BY sum(s.p) desc;

SELECT stock_name, 
    SUM(CASE WHEN operation = 'Buy' THEN price * (-1)
         ELSE price
    END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name
