-- lists all cities in database hbtn_0d_usa
-- Each record should display: cities.id /  cities.name /  states.name
-- results sorted in ascending order by cities.id
-- use only one SELECT statement / database passed as argument to mysql cli
SELECT cities.id, cities.name, states.name
  FROM cities
 INNER JOIN states ON cities.state_id = states.id
 ORDER BY cities.id ASC;