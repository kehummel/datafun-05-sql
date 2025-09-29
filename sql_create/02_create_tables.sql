CREATE TABLE authors (author_id NOT NULL PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL, birth_year NOT NULL);



CREATE TABLE books (book_id TEXT NOT NULL,
    title TEXT NOT NULL,
    year_published INTEGER,
    author_id TEXT NOT NULL)

