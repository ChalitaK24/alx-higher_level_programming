-- display the top 3 cities with the highest temperatures during July and August,
-- ordered by temperature in descending order
SELECT city, MAX(value) AS max_temperature FROM temperatures WHERE month IN (7, 8) GROUP BY cityORDER BY max_temperature DESC LIMIT 3;
