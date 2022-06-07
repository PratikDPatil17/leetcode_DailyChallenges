# Write your MySQL query statement below

# Facebook question to get percentage of healthy food 
#SELECT ROUND(AVG(CASE WHEN low_fats = 'Y' AND recyclable = 'Y' THEN 1 ELSE 0 END),2)*100 AS PERCENTAGE

SELECT
    product_id
FROM
    Products
WHERE
    low_fats = "Y" and recyclable = "Y"