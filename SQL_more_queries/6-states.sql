-- creates database hbtn_0d_usa & table states in MySQL server.
-- states description: id INT unique /  auto gen / not null  / primary key
-- name VARCHAR(256) not null / hbtn_0d_usa  exists ? no fail
-- table states exists ? no fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
