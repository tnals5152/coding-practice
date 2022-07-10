# Write your MySQL query statement below
SELECT b.id as id
FROM Weather as a, Weather as b
WHERE DATE_ADD(a.recordDate, INTERVAL 1 DAY) = b.recordDate
AND a.temperature < b.temperature
;
