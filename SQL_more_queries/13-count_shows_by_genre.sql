-- import database dump from hbtn_0d_tvshows (done in task 10)
-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- first column called genre / second column called number_of_shows
-- genre with no linked shows aren't display / database passed as arg to mysql cli
-- results sorted in descending order by the number of shows linked
SELECT tv_genres.name AS genre , COUNT(*) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
