<h3>SQL - Introduction</h3>

<h5>0. List databases</h5>

Write a script that lists all databases of your MySQL server.

<h5>1. Create a database</h5>

Write a script that creates the database hbtn_0c_0 in your MySQL server.

If the database hbtn_0c_0 already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements

<h5>2. Delete a database</h5>

Write a script that deletes the database hbtn_0c_0 in your MySQL server.

If the database hbtn_0c_0 doesn’t exist, your script should not fail
You are not allowed to use the SELECT or SHOW statements

<h5>3. List tables</h5>

Write a script that lists all the tables of a database in your MySQL server.

The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

<h5>4. First table</h5>

Write a script that creates a table called first_table in the current database in your MySQL server.

first_table description:
id INT
name VARCHAR(256)
The database name will be passed as an argument of the mysql command
If the table first_table already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements

<h5>5. Full description</h5>

Write a script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command
You are not allowed to use the DESCRIBE or EXPLAIN statements

<h5>6. List all in table</h5>

Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

All fields should be printed
The database name will be passed as an argument of the mysql command

<h5>7. First add</h5>

Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

New row:
id = 89
name = Best School
The database name will be passed as an argument of the mysql command

<h5>8. Count 89</h5>

Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command

<h5>9. Full creation</h5>

Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

second_table description:
id INT
name VARCHAR(256)
score INT
The database name will be passed as an argument to the mysql command
If the table second_table already exists, your script should not fail
You are not allowed to use the SELECT and SHOW statements
Your script should create these records:
id = 1, name = “John”, score = 10
id = 2, name = “Alex”, score = 3
id = 3, name = “Bob”, score = 14
id = 4, name = “George”, score = 8

<h5>10. List by best</h5>

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

Results should display both the score and the name (in this order)
Records should be ordered by score (top first)
The database name will be passed as an argument of the mysql command

<h5>11. Select the best</h5>

Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

Results should display both the score and the name (in this order)
Records should be ordered by score (top first)
The database name will be passed as an argument of the mysql command

<h5>12. Cheating is bad</h5>

Write a script that updates the score of Bob to 10 in the table second_table.

You are not allowed to use Bob’s id value, only the name field
The database name will be passed as an argument of the mysql command

<h5>13. Score too low</h5>

Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command

<h5>14. Average</h5>

Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

The result column name should be average
The database name will be passed as an argument of the mysql command

<h5>15. Number by score</h5>

Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

The result should display:
the score
the number of records for this score with the label number
The list should be sorted by the number of records (descending)
The database name will be passed as an argument to the mysql command

<h5>16. Say my name</h5>

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

Don’t list rows without a name value
Results should display the score and the name (in this order)
Records should be listed by descending score
The database name will be passed as an argument to the mysql command
In this example, new data have been added to the table second_table.

