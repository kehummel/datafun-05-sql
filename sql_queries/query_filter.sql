-- Show books where author was born before 1900

SELECT title
FROM authors_books
WHERE birth_year > 1900