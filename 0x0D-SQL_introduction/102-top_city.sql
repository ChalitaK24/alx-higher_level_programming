-- display the top 3 cities with the highest temperatures during July and August,
-- ordered by temperature in descending order
SELECT city, value AS temperature 
FROM temperatures 
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY temperature DESC
LIMIT 3;
