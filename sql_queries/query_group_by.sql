--Group by what century it was printed in and then bar graph it. 

SELECT first_name, last_name, year_published
FROM authors_books
GROUP BY year_published
HAVING COUNT(year_published) > 1900



