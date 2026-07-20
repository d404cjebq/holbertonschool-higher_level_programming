-- script that lists all records with a score >= 10
SELECT IF score >= 10, name FROM second_table
ORDER BY score DESC;
