-- finnds mathching records with same scores
SELECt score, COUNT(score) AS number FROM second_table
GROUP BY score ORDER BY score DESC;