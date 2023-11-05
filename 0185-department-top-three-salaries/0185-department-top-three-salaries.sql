SELECT _department.name 
AS Department, _employee.name 
AS Employee, salary 
AS Salary 
FROM (
SELECT *, dense_rank() over(
    PARTITION BY departmentId 
    ORDER BY salary DESC) 
    AS rk 
    FROM employee) _employee
    
JOIN department _department 
ON _employee.departmentId=_department.id
WHERE rk<=3