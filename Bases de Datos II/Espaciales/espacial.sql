--Instituto Tecnológico de Costa Rica
--Escuela de Ingeniería en Computación
--Curso de Bases de Datos II
--Profesora: Alicia Salazar Hernández
--Tarea Bases de datos espaciales
--Estudiante: Pedro Henrique Rodríguez de Oliveira (2013086585)
--II Semestre, 2016

--Código hecho para MariaDB/MySQL.

DELIMITER ;

DROP DATABASE test;

CREATE DATABASE test;

USE test;

CREATE TABLE IF NOT EXISTS calle(
       id INTEGER AUTO_INCREMENT primary key,
       nombre VARCHAR(20) not null,
       tamano VARCHAR(20) not null,
       forma LINESTRING not null
);

CREATE TABLE IF NOT EXISTS edificio(
       id INTEGER AUTO_INCREMENT primary key,
       nombre VARCHAR(20) not null,
       tipoComercio VARCHAR(20) not null,
       forma LINESTRING not null
);

CREATE TABLE IF NOT EXISTS edificioXcalle(
       idCalle INTEGER not null,
       idEdificio INTEGER not null,
       foreign key (idEdificio) references edificio (id),
       foreign key (idCalle) references calle (id)
);

DELIMITER //

CREATE PROCEDURE distanceBetweenPlaces(IN edificio1 VARCHAR(20), IN edificio2 VARCHAR(20))
BEGIN
	SELECT E.nombre, E2.nombre, ST_Distance(E.Forma, E2.forma) AS 'Distancia'
	FROM edificio E, edificio E2
	WHERE E.nombre = edificio1
	AND E2.nombre = edificio2;
END//

CREATE PROCEDURE neighbors(IN edificio1 VARCHAR(20))
BEGIN
	SELECT E.nombre, E2.nombre as 'Vecino'
	FROM edificio E, edificio E2
	WHERE ST_Touches(E.forma, E2.forma) = 1
	AND E.nombre = edificio1;
END//

CREATE PROCEDURE commerceLocation(IN edificio1 VARCHAR(20))
BEGIN
	SELECT E.nombre, ST_X(ST_StartPoint(E.forma)) AS 'X', ST_Y(ST_PointN(E.forma,3)) AS 'Y'
	FROM edificio E
	WHERE E.nombre = edificio1;
END//

CREATE PROCEDURE closerToMe(IN coordenadaX INTEGER, IN coordenadaY INTEGER, IN tipo VARCHAR(20))
BEGIN
	SELECT E.nombre, ST_Distance(Point(coordenadaX, coordenadaY), E.forma) AS 'Distancia'
	FROM edificio E
	WHERE E.tipoComercio = tipo
	ORDER BY Distancia ASC
	LIMIT 1;
END//
