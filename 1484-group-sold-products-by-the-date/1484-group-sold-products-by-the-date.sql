# Write your MySQL query statement below

SELECT
    sell_date, 
    count(DISTINCT product) as num_sold, 
    GROUP_CONCAT(DISTINCT product ORDER BY product) as products
    
    #(SELECT product from Activities where sell_date) as products
FROM
    Activities
GROUP BY
    sell_date
    

