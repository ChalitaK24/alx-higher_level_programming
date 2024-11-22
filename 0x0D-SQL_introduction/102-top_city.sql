-- display the top 3 cities with the highest temperatures during July and August,
-- ordered by temperature in descending order
SELECT city, value AS temperature 
FROM temperatures 
WHERE month IN (7, 8) 
ORDER BY value DESC 
LIMIT 3;
