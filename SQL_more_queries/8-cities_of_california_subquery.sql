-- lists all cities of cali that can be found in databse
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` = (
    SELECT `id` FROM `states`
    WHERE `name` = "California"
);