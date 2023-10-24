-- all cities found in databasse
SELECT cities.id, cities.name, states.name
FROM cities LEFT JOIN states
ON cities.state_id = state.id;