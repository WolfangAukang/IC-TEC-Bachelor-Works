--DUMMY DATA
INSERT INTO CATEGORIES(category) VALUES('Romantic');
INSERT INTO CATEGORIES(category) VALUES('Action');
INSERT INTO CATEGORIES(category) VALUES('Drama');
INSERT INTO CATEGORIES(category) VALUES('Comedy');
INSERT INTO CATEGORIES(category) VALUES('Terror');

INSERT INTO MOVIES(title, id_category) VALUES('Titanic', 1);
INSERT INTO MOVIES(title, id_category) VALUES('Fight Club', 2);
INSERT INTO MOVIES(title, id_category) VALUES('Kill Bill Vol.1', 2);
INSERT INTO MOVIES(title, id_category) VALUES('Memento', 3);
INSERT INTO MOVIES(title, id_category) VALUES('Pineapple Express', 4);
INSERT INTO MOVIES(title, id_category) VALUES('The Ring', 5);

INSERT INTO CLIENTS(full_name) VALUES('Jorge González');
INSERT INTO CLIENTS(full_name) VALUES('Ana Masis');
INSERT INTO CLIENTS(full_name) VALUES('Ricardo Montero');
INSERT INTO CLIENTS(full_name) VALUES('Andrey Vega');

INSERT INTO RENTS(id_movie, id_client, rent_date, amount) VALUES (1,4,'2016-02-28 12:30:00',2000);
INSERT INTO RENTS(id_movie, id_client, rent_date, amount) VALUES (2,3,'2016-03-03 10:45:00',500);
INSERT INTO RENTS(id_movie, id_client, rent_date, amount) VALUES (1,1,'2016-04-12 18:34:00',1000);
INSERT INTO RENTS(id_movie, id_client, rent_date, amount) VALUES (6,3,'2016-05-01 13:09:00',2000);
INSERT INTO RENTS(id_movie, id_client, rent_date, amount) VALUES (3,3,'2016-06-15 17:23:00',500);
INSERT INTO RENTS(id_movie, id_client, rent_date, amount) VALUES (5,2,'2016-06-30 09:15:00',1000);
INSERT INTO RENTS(id_movie, id_client, rent_date, amount) VALUES (4,2,'2016-07-28 18:59:00',1500);
INSERT INTO RENTS(id_movie, id_client, rent_date, amount) VALUES (6,4,NOW(),1000);

--FULL TABLE INFO
SELECT 'LISTA ORIGINAL' AS Msg;
SELECT R.id_rent, M.title, CT.category, C.full_name, R.rent_date, R.amount FROM RENTS R
LEFT JOIN MOVIES M ON M.id_movie = R.id_movie
LEFT JOIN CATEGORIES CT ON CT.id_category = M.id_category
LEFT JOIN CLIENTS C ON C.id_client = R.id_client;

DELIMITER //
CREATE PROCEDURE totalCountPerDate (IN pInitialDate DATE, IN pFinishDate DATE)
BEGIN
    SELECT 'TOTAL DE VIDEOS RENTADOS' AS Msg;
    
    SELECT 'TOTAL DE VIDEOS RENTADOS X CATEGORIA' AS Msg;
    SELECT CT.category, COUNT(*) FROM RENTS R
    LEFT JOIN MOVIES M ON M.id_movie = R.id_movie
    LEFT JOIN CATEGORIES CT ON CT.id_category = M.id_category
    WHERE (R.rent_date BETWEEN pInitialDate AND pFinishDate)
    GROUP BY CT.category
    WITH ROLLUP;

    SELECT 'TOTAL DE VIDEOS RENTADOS X CLIENTE' AS Msg;
    SELECT C.full_name, COUNT(*) FROM RENTS R
    LEFT JOIN CLIENTS C ON C.id_client = R.id_client
    WHERE (R.rent_date BETWEEN pInitialDate AND pFinishDate)
    GROUP BY C.full_name
    WITH ROLLUP;

    SELECT 'CROSS FINGERUS' AS Msg;

    SELECT CT.category, C.full_name, COUNT(CT.category) AS cantidad FROM RENTS R
    LEFT JOIN MOVIES M ON M.id_movie = R.id_movie
    LEFT JOIN CATEGORIES CT ON CT.id_category = M.id_category
    LEFT JOIN CLIENTS C ON C.id_client = R.id_client
    WHERE (R.rent_date BETWEEN pInitialDate AND pFinishDate)
    GROUP BY CT.category, C.full_name
    WITH ROLLUP;
END//

CREATE PROCEDURE totalAmountPerDate (IN pInitialDate DATE, IN pFinishDate DATE)
BEGIN
    SELECT 'TOTAL DE VIDEOS RENTADOS X CATEGORIA' AS Msg;
    SELECT CT.category, SUM(R.amount) FROM RENTS R
    LEFT JOIN MOVIES M ON M.id_movie = R.id_movie
    LEFT JOIN CATEGORIES CT ON CT.id_category = M.id_category
    WHERE (R.rent_date BETWEEN pInitialDate AND pFinishDate)
    GROUP BY CT.category
    WITH ROLLUP;

    SELECT 'TOTAL DE VIDEOS RENTADOS X CLIENTE' AS Msg;
    SELECT C.full_name, SUM(R.amount) FROM RENTS R
    LEFT JOIN CLIENTS C ON C.id_client = R.id_client
    WHERE (R.rent_date BETWEEN pInitialDate AND pFinishDate)
    GROUP BY C.full_name
    WITH ROLLUP;
END//

DELIMITER ;
