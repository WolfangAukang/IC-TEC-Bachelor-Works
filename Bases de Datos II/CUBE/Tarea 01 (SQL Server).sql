--Instituto Tecnológico de Costa Rica
--Escuela de Ingeniería en Computación
--Curso de Bases de Datos II
--Profesora: Alicia Salazar Hernández
--Tarea 01
--Estudiante: Pedro Henrique Rodríguez de Oliveira (2013086585)
--II Semestre, 2016
 
--Código hecho para SQL Server. Se utilizó la base de datos BD_TOKENIZE del ecrhin.ec.tec.ac.cr\Estudiantes
 
use BD_TOKENIZE;
 
CREATE TABLE CATEGORIES
(
  id_category INTEGER IDENTITY(1,1) PRIMARY KEY,
  category VARCHAR(20)
);
 
CREATE TABLE MOVIES
(
  id_movie INTEGER IDENTITY(1,1) PRIMARY KEY,
  title VARCHAR(50) NOT NULL,
  id_category INTEGER NOT NULL
);
 
ALTER TABLE MOVIES
ADD FOREIGN KEY (id_category) REFERENCES CATEGORIES(id_category);
 
CREATE TABLE CLIENTS
(
  id_client INTEGER NOT NULL IDENTITY(1,1) PRIMARY KEY,
  full_name VARCHAR(100) NOT NULL
);
 
CREATE TABLE  RENTS
(
  id_rent INTEGER NOT NULL IDENTITY(1,1) PRIMARY KEY,
  id_movie INTEGER NOT NULL,
  id_client INTEGER NOT NULL,
  rent_date DATETIME NOT NULL,
  amount REAL NOT NULL
);
 
ALTER TABLE RENTS
ADD FOREIGN KEY (id_movie) REFERENCES MOVIES(id_movie);

ALTER TABLE RENTS
ADD FOREIGN KEY (id_client) REFERENCES CLIENTS(id_client);


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
INSERT INTO RENTS(id_movie, id_client, rent_date, amount) VALUES (6,4,CURRENT_TIMESTAMP,1000);


CREATE PROCEDURE usp_totalOrderQuantity @pInitialDate DATETIME, @pFinalDate DATETIME 
AS
BEGIN
	SELECT CT.category, C.full_name, COUNT(*) AS cantidad FROM RENTS R
	LEFT JOIN MOVIES M ON M.id_movie = R.id_movie
	LEFT JOIN CATEGORIES CT ON CT.id_category = M.id_category
	LEFT JOIN CLIENTS C ON C.id_client = R.id_client
	WHERE (R.rent_date BETWEEN @pInitialDate AND @pFinalDate)
	GROUP BY CT.category, C.full_name
	WITH CUBE
	ORDER BY C.full_name;
END;

CREATE PROCEDURE usp_totalOrderAmount @pInitialDate DATETIME, @pFinalDate DATETIME 
AS
BEGIN
	SELECT CT.category, C.full_name, SUM(R.amount) AS cantidad FROM RENTS R
	LEFT JOIN MOVIES M ON M.id_movie = R.id_movie
	LEFT JOIN CATEGORIES CT ON CT.id_category = M.id_category
	LEFT JOIN CLIENTS C ON C.id_client = R.id_client
	WHERE (R.rent_date BETWEEN @pInitialDate AND @pFinalDate)
	GROUP BY CT.category, C.full_name
	WITH CUBE
	ORDER BY C.full_name;
END;