-- import database dump from hbtn_0d_tvshows (done in task 10)
-- lists all shows contained in hbtn_0d_tvshows without a genre linked
-- each record display: tv_shows.title / tv_show_genres.genre_id
-- results sorted in ascending order by tv_shows.title & tv_show_genres.genre_id
-- database passed as argument to mysql cli
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows
  LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
 WHERE tv_show_genres.genre_id IS NULL
 ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;