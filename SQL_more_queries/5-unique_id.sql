-- creates the table unique_id on MySQL server.
-- unique_id description: id INT / default value 1 / must be unique / name VARCHAR(256)
-- database passed as an argument to mysql cli / table unique_id ? no fail
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);