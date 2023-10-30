# Write your MySQL query statement below
select 
person_name
from Queue q
where 1000>= (select sum(weight) from Queue where q.turn>= turn)
order by turn desc
limit 1;