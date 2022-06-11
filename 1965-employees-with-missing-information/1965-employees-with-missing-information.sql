# Write your MySQL query statement below


SELECT T.employee_id from
(
    SELECT * FROM Employees 
    UNION ALL
    SELECT * FROM Salaries
) T

GROUP BY T.EMPLOYEE_ID
HAVING COUNT(T.EMPLOYEE_ID) = 1   /*can also use count(*) */
ORDER BY T.EMPLOYEE_ID ASC
