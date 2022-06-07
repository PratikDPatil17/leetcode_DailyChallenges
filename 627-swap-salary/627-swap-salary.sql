# Write your MySQL query statement below


UPDATE Salary
    SET sex = (Case sex 
                WHEN 'm' then 'f'
                ELSE 'm'
              END ) 
    
