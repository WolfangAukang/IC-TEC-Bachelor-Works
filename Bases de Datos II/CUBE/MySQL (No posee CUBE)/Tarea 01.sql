--Instituto Tecnológico de Costa Rica
--Escuela de Ingeniería en Computación
--Curso de Bases de Datos II
--Profesora: Alicia Salazar Hernández
--Tarea 01
--Estudiante: Pedro Henrique Rodríguez de Oliveira (2013086585)
--II Semestre, 2016

--Código hecho para MariaDB/MySQL.

CREATE DATABASE tarea01;
USE tarea01;

CREATE TABLE IF NOT EXISTS CATEGORIES
(
  id_category INTEGER,
  category VARCHAR(20)
);

ALTER TABLE CATEGORIES
MODIFY id_category INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY;

CREATE TABLE IF NOT EXISTS MOVIES
(
  id_movie INTEGER,
  title VARCHAR(50) NOT NULL,
  id_category INTEGER NOT NULL
);

ALTER TABLE MOVIES
MODIFY id_movie INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
ADD FOREIGN KEY (id_category) REFERENCES CATEGORIES(id_category);

CREATE TABLE IF NOT EXISTS CLIENTS
(
  id_client INTEGER NOT NULL,
  full_name VARCHAR(100) NOT NULL
);

ALTER TABLE CLIENTS
MODIFY id_client INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY;

CREATE TABLE IF NOT EXISTS RENTS
(
  id_rent INTEGER NOT NULL,
  id_movie INTEGER NOT NULL,
  id_client INTEGER NOT NULL,
  rent_date DATETIME NOT NULL,
  amount REAL NOT NULL
);

ALTER TABLE RENTS
MODIFY id_rent INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
ADD FOREIGN KEY (id_movie) REFERENCES MOVIES(id_movie),
ADD FOREIGN KEY (id_client) REFERENCES CLIENTS(id_client);
