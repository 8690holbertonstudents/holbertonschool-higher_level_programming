-- import database dump from hbtn_0d_tvshows to MySQL server
-- lists all shows in hbtn_0d_tvshows with at least one genre linked
-- each record should display: tv_shows.title / tv_show_genres.genre_id
-- results sorted in ascending order by tv_shows.title & tv_show_genres.genre_id
-- use only one SELECT statement / database will be passed as an arg to mysql command
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows
 INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
 ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;