-- import database dump from hbtn_0d_tvshows (done ata task 10)
-- lists all Comedy shows in the database hbtn_0d_tvshows
-- the tv_genres table contains only one record where name = Comedy
-- each record should display: tv_shows.title
-- results sorted in ascending order by the show title
-- database passed as arg to mysql cli
SELECT tv_shows.title
  FROM tv_shows
 INNER JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
 INNER JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id
 WHERE tv_genres.name = "Comedy"
 ORDER BY tv_shows.title ASC;