CREATE TABLE wishlist (user TEXT NOT NULL, product_id INTEGER REFERENCES products(id));
