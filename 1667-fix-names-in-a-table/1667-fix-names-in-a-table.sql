# Write your MySQL query statement below
SELECT
    user_id,
    #CONCAT(upper(left(name,1)), lower(substring(name,2))) as name
    CONCAT(upper(left(name,1)), lower(right(name,length(name)-1))) as name
    
FROM
    Users
ORDER BY
    user_id