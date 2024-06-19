-- import database dump from hbtn_0d_tvshows (done on task 10)
-- lists all shows, and all genres linked to that show, from hbtn_0d_tvshows
-- if show doesn’t have a genre, display NULL in the genre column
-- each record display: tv_shows.title / tv_genres.name
-- results sorted ascending order by the show title and genre name
-- database name will be passed as an argument of the mysql command
SELECT tv_shows.title, tv_genres.name
  FROM tv_shows
  LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
  LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
 ORDER BY tv_shows.title ASC, tv_genres.name ASC;