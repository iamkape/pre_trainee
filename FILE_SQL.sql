--Display the number of films in each category, sorted in descending order.
SELECT
	C.NAME,
	COUNT(FC.FILM_ID) AS COUNT_FILM
FROM
	CATEGORY C
	LEFT JOIN FILM_CATEGORY FC ON C.CATEGORY_ID = FC.CATEGORY_ID
GROUP BY
	C.NAME
ORDER BY
	COUNT_FILM DESC;

--Display the top 10 actors whose films were rented the most, sorted in descending order.
SELECT
	A.FIRST_NAME,
	A.LAST_NAME,
	SUM(F.RENTAL_DURATION) AS SUM_RENTAL_DURATION
FROM
	ACTOR A
	LEFT JOIN FILM_ACTOR FA ON A.ACTOR_ID = FA.ACTOR_ID
	LEFT JOIN FILM F ON FA.FILM_ID = F.FILM_ID
GROUP BY
	A.FIRST_NAME,
	A.LAST_NAME,
	F.RENTAL_DURATION
ORDER BY
	SUM_RENTAL_DURATION DESC
LIMIT
	10;

--Display the category of films that generated the highest revenue.
SELECT
	C.NAME,
	SUM(F.RENTAL_DURATION * F.RENTAL_RATE) AS TOTAL_COST
FROM
	CATEGORY C
	LEFT JOIN FILM_CATEGORY FC ON C.CATEGORY_ID = FC.CATEGORY_ID
	LEFT JOIN FILM F ON FC.FILM_ID = F.FILM_ID
GROUP BY
	C.NAME,
	F.RENTAL_DURATION,
	F.RENTAL_RATE
ORDER BY
	TOTAL_COST DESC
LIMIT
	1;

--Display the titles of films not present in the inventory. Write the query without using the IN operator.
SELECT DISTINCT
	F.TITLE
FROM
	FILM F
	LEFT JOIN INVENTORY I ON F.FILM_ID = I.FILM_ID
WHERE
	I.FILM_ID IS NULL;

--Display the top 3 actors who appeared the most in films within the "Children" category. 
--If multiple actors have the same count, include all.
SELECT
	A.FIRST_NAME,
	A.LAST_NAME,
	COUNT(*) AS SUM_ROLES
FROM
	ACTOR A
	INNER JOIN (
		SELECT
			FA.ACTOR_ID
		FROM
			FILM_ACTOR FA
			INNER JOIN FILM_CATEGORY FC ON FA.FILM_ID = FC.FILM_ID
			INNER JOIN CATEGORY C ON FC.CATEGORY_ID = C.CATEGORY_ID
		WHERE
			C.NAME = 'Children'
	) AS CHILDREN_ACTORS ON A.ACTOR_ID = CHILDREN_ACTORS.ACTOR_ID
GROUP BY
	A.FIRST_NAME,
	A.LAST_NAME
ORDER BY
	SUM_ROLES DESC
LIMIT
	6;

--Display cities with the count of active and inactive customers (active = 1). 
--Sort by the count of inactive customers in descending order.
SELECT
	C.CITY,
	COUNT(CASE WHEN CST.ACTIVE = 1 THEN 1 END) AS ACTIVE_CUSTOMERS,
	COUNT(CASE WHEN CST.ACTIVE = 0 THEN 1 END) AS INACTIVE_CUSTOMERS
FROM
	CITY C
	JOIN ADDRESS A ON C.CITY_ID = A.CITY_ID
	JOIN CUSTOMER CST ON A.ADDRESS_ID = CST.ADDRESS_ID
GROUP BY
	C.CITY
ORDER BY
	INACTIVE_CUSTOMERS DESC;

--Display the film category with the highest total rental hours in cities
--where customer.address_id belongs to that city and starts with the letter "a".
--Do the same for cities containing the symbol "-". Write this in a single query.
