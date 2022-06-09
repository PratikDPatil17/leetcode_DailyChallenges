# Write your MySQL query statement below
#SELECT * FROM patients WHERE conditions REGEXP '\\bDIAB1'

SELECT *
FROM Patients
WHERE conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%'


