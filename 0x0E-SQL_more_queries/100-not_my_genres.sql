-- Uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT  tv_genres.name
FROM tv_genres 
WHERE  tv_genres.id NOT IN (SELECT  tv_show_genres.genre_id)
ORDER BY tv_genres.name ASC;
