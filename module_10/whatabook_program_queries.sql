

SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
    INNER JOIN user ON wishlist.user_id = user.user_id
    INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;

/*
    Query to select all locations
*/
SELECT store_id, locale from store;

/*
    Query to select all books in whatabook store
*/
SELECT book_id, book_name, author, details from book;

/*
    query to select what is not in the users wishlist
*/
SELECT book_id, book_name, author, details
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = 1);

/*
  Query to insert a book into user's wishli
  
*/
INSERT INTO wishlist(user_id, book_id)
    VALUES(1, 9)

/*
   Query to remove a book from user's wishlist
*/
DELETE FROM wishlist WHERE user_id = 1 AND book_id = 9;