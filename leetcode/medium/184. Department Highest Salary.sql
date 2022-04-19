# Write your MySQL query statement below
select d2.name as Department, e2.name as Employee, e2.salary as Salary
from (select d.id, d.name, max(e.salary) as max_salary
    from employee e, department d
    where e.departmentId = d.id
    group by d.name) d2 inner join employee e2
where e2.departmentId = d2.id
and e2.salary = max_salary;
