--Join books into authors

CREATE TABLE IF NOT EXISTS authors_books AS
SELECT authors.first_name, authors.last_name, authors.birth_year, books.title, books.year_published
FROM books
INNER JOIN authors ON books.author_id = authors.author_id;
