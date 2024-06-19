-- lists all  California cities found in database hbtn_0d_usa
-- states table contains only one record where name = California
-- Results must be sorted in ascending order by cities.id
-- database name  passed as an argument to mysql cli
SELECT id, name
  FROM cities
 WHERE state_id = (
    SELECT id
      FROM states
     WHERE name = "California"
 )
ORDER BY id ASC;