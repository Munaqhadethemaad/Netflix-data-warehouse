CREATE OR REPLACE VIEW view_titles_by_genre AS
SELECT TRIM(SPLIT_PART(listed_in, ',', 1)) AS genre,
       COUNT(*) AS title_count
FROM raw_titles
GROUP BY genre
ORDER BY title_count DESC;

CREATE OR REPLACE VIEW view_titles_by_country AS
SELECT TRIM(SPLIT_PART(country, ',', 1)) AS country,
       COUNT(*) AS title_count
FROM raw_titles
GROUP BY country
ORDER BY title_count DESC;

CREATE OR REPLACE VIEW view_titles_by_year AS
SELECT release_year,
       COUNT(*) AS title_count
FROM raw_titles
GROUP BY release_year
ORDER BY release_year;
