-- import the database dump of hbtn_0d_tvshows (done in task 10)
-- lists all shows contained in database hbtn_0d_tvshows
-- each record display tv_shows.title / tv_show_genres.genre_id
-- sorted in ascending order by tv_shows.title & tv_show_genres.genre_id
-- if show have no genre, display NULL / database passed as arg to mysql command
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows
  LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
 ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;