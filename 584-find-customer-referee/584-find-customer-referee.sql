# Write your MySQL query statement below
SELECT
    name
FROM
    Customer
#WHERE
#    referee_id != 2 OR referee_id is NULL
    
WHERE
    COALESCE(referee_id, 0) <> 2