# Write your MySQL query statement below
select round(sum(tiv_2016),2) as tiv_2016
from Insurance a
where a.tiv_2015 in (Select tiv_2015 from Insurance where pid <> a.pid)
and
(a.lat,a.lon) not in (select lat,lon from Insurance where pid<>a.pid)