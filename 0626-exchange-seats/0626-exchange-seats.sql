# Write your MySQL query statement below
select id,
case when id%2=0 then (lag(student) over (order by id))
else ifnull(lead(student) over (order by id), student)
end as student
from seat