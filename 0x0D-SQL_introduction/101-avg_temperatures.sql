-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) AS average_temperature FROM temperatures GROUP BY cityORDER BY average_temperature DESC;:
