# Write your MySQL query statement below
select em2.employee_id,
 em2.name,
count(*) as reports_count,
round(avg(em1.age)) as average_age
from Employees em1 inner join Employees em2
on em1.reports_to = em2.employee_id
group by em2.employee_id
order by em2.employee_id