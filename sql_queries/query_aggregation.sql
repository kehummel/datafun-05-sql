--find age when published and put into column age_when_published
--scatter plot of age vs year printed? 

SELECT year_published, year_published - birth_year as age_when_published 
FROM authors_books