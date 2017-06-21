--Instituto Tecnológico de Costa Rica
--Escuela de Ingeniería en Computación
--Curso de Bases de Datos II
--Profesora: Alicia Salazar Hernández
--Competencia Uber
--Estudiante: Myron Camacho Brenes (2013)
--            Pedro Rodríguez de Oliveira (2013086585)
--II Semestre, 2016

--Código hecho para MariaDB/MySQL.
--Si se remueve la palabra EXPLAIN del inicio de cada comando del procedure, se obtiene el código a ejecutar


--1: Crear base de datos
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema EmpresaTransportes
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `EmpresaTransportes` ;

-- -----------------------------------------------------
-- Schema EmpresaTransportes
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `EmpresaTransportes` DEFAULT CHARACTER SET utf8 ;
USE `EmpresaTransportes` ;

-- -----------------------------------------------------
-- Table `EmpresaTransportes`.`TipoTransporte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EmpresaTransportes`.`TipoTransporte` (
  `idTipoTransporte` TINYINT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(30) NULL,
  `porcentajeXKilometro` DOUBLE NULL,
  PRIMARY KEY (`idTipoTransporte`))
ENGINE = InnoDB;


-- La tabla de estados
-- 1: Activo
-- 2: Notificado
-- 3: Suspendido
-- 4: Post-Suspendido
CREATE TABLE IF NOT EXISTS Estado(
	idEstado TINYINT NOT NULL,
    descripcion VARCHAR(15),
    PRIMARY KEY(idEstado)
);

-- -----------------------------------------------------
-- Table `EmpresaTransportes`.`Chofer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EmpresaTransportes`.`Chofer` (
  `idChofer` TINYINT NOT NULL,
  `nombre` VARCHAR(25) NULL,
  `primerApellido` VARCHAR(25) NULL,
  `segundoApellido` VARCHAR(25) NULL,
  `placa` VARCHAR(9) NULL,
  PRIMARY KEY (`idChofer`),
  UNIQUE INDEX `placa_UNIQUE` (`placa` ASC))
ENGINE = InnoDB;

ALTER TABLE Chofer
ADD idEstado TINYINT;

ALTER TABLE Chofer
ADD CONSTRAINT fk_Estado FOREIGN KEY (idEstado) REFERENCES Estado(idEstado);


-- -----------------------------------------------------
-- Table `EmpresaTransportes`.`Dia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EmpresaTransportes`.`Dia` (
  `idDia` TINYINT NOT NULL AUTO_INCREMENT,
  `dia` VARCHAR(15) NULL,
  PRIMARY KEY (`idDia`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `EmpresaTransportes`.`Horarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EmpresaTransportes`.`Horarios` (
  `idHorarios` TINYINT NOT NULL AUTO_INCREMENT,
  `horaInicio` TIME NULL,
  `horaFin` TIME NULL,
  `idChofer` TINYINT NOT NULL,
  `idDia` TINYINT NOT NULL,
  PRIMARY KEY (`idHorarios`),
  INDEX `fk_Horarios_Chofer1_idx` (`idChofer` ASC),
  INDEX `fk_Horarios_Dia1_idx` (`idDia` ASC),
  CONSTRAINT `fk_Chofer`
    FOREIGN KEY (`idChofer`)
    REFERENCES `EmpresaTransportes`.`Chofer` (`idChofer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Dia`
    FOREIGN KEY (`idDia`)
    REFERENCES `EmpresaTransportes`.`Dia` (`idDia`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `EmpresaTransportes`.`Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EmpresaTransportes`.`Cliente` (
  `idCliente` TINYINT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(25) NULL,
  `primerApellido` VARCHAR(25) NULL,
  `segundoApellido` VARCHAR(25) NULL,
  PRIMARY KEY (`idCliente`))
ENGINE = InnoDB;

ALTER TABLE Cliente
ADD puntos DOUBLE;

-- -----------------------------------------------------
-- Table `EmpresaTransportes`.`Servicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EmpresaTransportes`.`Servicio` (
  `idServicio` TINYINT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NULL,
  `puntoPartida` POINT NULL,
  `puntoLLegada` POINT NULL,
  `porcentajeMonto` DOUBLE NULL,
  `idCliente` TINYINT NOT NULL,
  `idChofer` TINYINT NOT NULL,
  PRIMARY KEY (`idServicio`),
  INDEX `fk_Servicio_Cliente1_idx` (`idCliente` ASC),
  INDEX `fk_Servicio_Chofer1_idx` (`idChofer` ASC),
  CONSTRAINT `fk_idCliente`
    FOREIGN KEY (`idCliente`)
    REFERENCES `EmpresaTransportes`.`Cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_idChofer`
    FOREIGN KEY (`idChofer`)
    REFERENCES `EmpresaTransportes`.`Chofer` (`idChofer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `EmpresaTransportes`.`Vehiculo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EmpresaTransportes`.`Vehiculo` (
  `idVehiculo` TINYINT NOT NULL AUTO_INCREMENT,
  `marca` VARCHAR(45) NULL,
  `idChofer` TINYINT NOT NULL,
  `idTipoTransporte` TINYINT NOT NULL,
  PRIMARY KEY (`idVehiculo`),
  INDEX `fk_Vehiculo_Chofer1_idx` (`idChofer` ASC),
  INDEX `fk_Vehiculo_TipoTransporte1_idx` (`idTipoTransporte` ASC),
  CONSTRAINT `fk_Chofer_Vehiculo`
    FOREIGN KEY (`idChofer`)
    REFERENCES `EmpresaTransportes`.`Chofer` (`idChofer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TipoTransporte_Vehiculo`
    FOREIGN KEY (`idTipoTransporte`)
    REFERENCES `EmpresaTransportes`.`TipoTransporte` (`idTipoTransporte`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `EmpresaTransportes`.`Calificacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EmpresaTransportes`.`Calificacion` (
  `idCalificacion` INT NOT NULL AUTO_INCREMENT,
  `calificacion` DOUBLE NULL,
  `idServicio` TINYINT NOT NULL,
  `idChofer` TINYINT NOT NULL,
  PRIMARY KEY (`idCalificacion`),
  INDEX `fk_Calificacion_Servicio1_idx` (`idServicio` ASC),
  INDEX `fk_Calificacion_Chofer1_idx` (`idChofer` ASC),
  CONSTRAINT `fk_Servicio`
    FOREIGN KEY (`idServicio`)
    REFERENCES `EmpresaTransportes`.`Servicio` (`idServicio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Chofer_Calificacion`
    FOREIGN KEY (`idChofer`)
    REFERENCES `EmpresaTransportes`.`Chofer` (`idChofer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `EmpresaTransportes`.`Rango`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EmpresaTransportes`.`Rango` (
  `idRango` INT NOT NULL AUTO_INCREMENT,
  `inicio` FLOAT NULL,
  `fin` FLOAT NULL,
  `monto` DOUBLE NULL,
  PRIMARY KEY (`idRango`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `EmpresaTransportes`.`ClienteFrecuente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EmpresaTransportes`.`ClienteFrecuente` (
  `idClienteFrecuente` TINYINT NOT NULL AUTO_INCREMENT,
  `puntos` DOUBLE NULL,
  `idCliente` TINYINT NOT NULL,
  PRIMARY KEY (`idClienteFrecuente`),
  INDEX `fk_ClienteFrecuente_Cliente1_idx` (`idCliente` ASC),
  CONSTRAINT `fk_Cliente_ClienteFrecuente`
    FOREIGN KEY (`idCliente`)
    REFERENCES `EmpresaTransportes`.`Cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

DROP TABLE ClienteFrecuente;




SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

DELIMITER //

--2: Ingreso, actualización y consulta de choferes
CREATE PROCEDURE pAgregarChofer(IN pId INTEGER, IN pNombre VARCHAR(30), IN pTipoVehiculo INTEGER, IN pPlaca VARCHAR(9), IN pDia INTEGER, IN pHoraInicio TIME, IN pHoraFin TIME)
BEGIN
	EXPLAIN INSERT INTO chofer(idChofer, nombre, calificacion, placa, idTipoDeVehiculo)
	VALUES(pId, pNombre, 0.00, pPlaca, pTipoVehiculo);
        EXPLAIN INSERT INTO horario(idChofer, horaInicio, horaFin, idDia)
        VALUES(pId, pHoraInicio, pHoraFin,
	pDia);

	--Explicación: En este caso se explicarán dos comandos INSERT que se ejecutarán.
	--En ambos, el explain es rápido por la cuestión de la llave primaria siendo manejada por INTEGER, con un tiempo de 0.01s
	--En cuestión de ser una inserción, lo único que se verifica es que no se repitan cuestiones como la placa. Por lo que ahí podría estar lo duradero del procedimiento.
	--Sin embargo, esto solo se aplica a lo primero por el número de placa.
END//

CREATE PROCEDURE pActualizarChofer(IN pId INTEGER, IN pNombre VARCHAR(30), IN pTipoVehiculo INTEGER, IN pPlaca VARCHAR(9), IN pDia INTEGER, IN pHoraInicio TIME, IN pHoraFin TIME)
BEGIN
  EXPLAIN UPDATE chofer
  SET nombre = COALESCE(pNombre, nombre),
      placa = COALESCE(pPlaca, placa),
      idTipoDeVehiculo = (pTipoVehiculo, idTipoDeVehiculo)
  WHERE idChofer = pId;

  EXPLAIN UPDATE horario
  SET horaInicio = COALESCE(pHoraInicio, horaInicio),
      horaFin = COALESCE(pHoraFin, horaFin),
      idDia = COALESCE(pDia, idDia)
  WHERE idChofer = pId;

  --En ambos updates, se está haciendo uso del coalesce para hacer más efectivo el uso de los parámetros, caso estos sean nulos.
  --El tiempo según el explain es de 0.01, esto por ser un UPDATE donde hay que buscar valores.
END//

CREATE PROCEDURE pConsultarChofer(IN pNombre VARCHAR(30), IN pCalificacion NUMERIC(3), IN pTipoVehiculo INTEGER, IN pPlaca VARCHAR(9), IN pDia INTEGER, IN pHoraInicio TIME, IN pHoraFin TIME)
BEGIN
  EXPLAIN SELECT C.nombre, C.calificacion, V.descripcion, C.placa, D.descripcion, H.horaInicio, H.horaFin
  FROM chofer C
  INNER JOIN tipoVehiculo V
  ON V.idTipo = C.idTipoDeVehiculo
  INNER JOIN horario H
  ON H.idChofer = C.idChofer
  INNER JOIN dia D
  ON D.idDia = H.idDia
  WHERE C.nombre = COALESCE(pNombre, C.nombre) AND
        C.calificacion = COALESCE(pCalificacion, C.calificacion) AND
        C.placa = COALESCE(pPlaca, C.placa) AND
        H.horaInicio = COALESCE(pHoraInicio, H.horaInicio) AND
        H.horaFin = COALESCE(pHoraFin, H.horaFin) AND
        V.idTipo = COALESCE(pTipoVehiculo, V.idTipo) AND
        D.idDia = COALESCE(pDia, D.idDia);
END//

  --Acá, por se un select algo más complejo por los COALESCE, el rpocedure toma su tiempo para buscar los resultados. Sin embargo, dura 0.00 por el tamaño de la tabla

--3: Calificar chofer
CREATE PROCEDURE pCalificarChofer(IN pId INTEGER, IN pCalificacion NUMERIC(3))
BEGIN
  EXPLAIN UPDATE chofer
  SET calificacion = COALESCE(pCalificacion, calificacion)
  WHERE idChofer = pId;

  -- Como es un update sencillo, se toma su tiempo buscando a cuál id modificar la calificación
END//


-- Realice un procedimiento que obtenga los choferes que hay que llamarles 
-- la atención o que haya que suspender o eliminar de la bd de proveedores

DELIMITER //
DROP PROCEDURE IF EXISTS consultar_choferes_amonestados //
CREATE PROCEDURE consultar_choferes_amonestados()
BEGIN
    EXPLAIN SELECT ch.nombre, ch.primerApellido, ch.segundoApellido, CalificacionTotal 
    FROM Chofer ch INNER JOIN Calificacion ca
    ON ch.idChofer = ca.idChofer
    WHERE (SELECT AVG(ca.calificacion) AS CalificacionTotal FROM ca 
    WHERE ca.idChofer = ch.idChofer) <= 3.0;

    EXPLAIN SELECT ch.nombre,ch.primerApellido, ch.segundoApellido
    FROM Chofer ch INNER JOIN Calificacion ca
    ON ch.idChofer = ca.idChofer
    WHERE(SELECT AVG(ca.calificacion) FROM ca
    INNER JOIN Servicio s
    ON ca.idServicio = s.idServicio
    WHERE ca.idChofer = ch.idChofer AND 
    (SELECT TIMESTAMPDIFF(MONTH, CURDATE(), s.fecha) ) >= 2 
    ) <= 3.0;
    
    EXPLAIN SELECT ch.nombre, ch.primerApellido, ch.segundoApellido, CalificacionTotal FROM Chofer ch
    INNER JOIN Calificacion ca
    ON ch.idChofer = ca.idChofer
	WHERE ch.idEstado = 4 AND (SELECT AVG(ca.calificacion) AS CalificacionTotal FROM ca 
    WHERE ca.idChofer = ch.idChofer) <= 3.0;

  --Se creó un índice en la tabla de calificaciones debido a que un chofer tendrá varias calificaciones, esto con el fin de optimizar las consultas que se hacen.
  --Las consultas se realizan con inner joins en todo lo posible y la clausula where se ejecuta cuando ya se han reducido los registros a revisar.
    
END//

-- Realice un procedimiento para hacer ingreso, actualización de clientes

DELIMITER //
DROP PROCEDURE IF EXISTS insertar_actualizar_cliente //
CREATE PROCEDURE insertar_actualizar_cliente(pIdCliente TINYINT,pNombre VARCHAR(25), pPrimerApellido VARCHAR(25),
 pSegundoApellido VARCHAR(25) )
 BEGIN
	EXPLAIN INSERT INTO Cliente(idCliente, nombre, primerApellido, segundoApellido)
    VALUES(pIdCliente, pNombre, pPrimerApellido, pSegundoApellido)
    ON DUPLICATE KEY UPDATE nombre = pNombre, primerApellido = pPrimerApellido, 
    segundoApellido = pSegundoApellido;

--Para este procedure se hace uso de una función de mysql que revisa si el cliente que se va a insertar ya existe, y si es el caso solo actualiza los campos del cliente. Se hace de esta forma para evitar primero consultar por el cliente y luego revisar si existe o no, y en caso de que exista actualizarlo y sino insertar uno nuevo. Es más óptimo solo utilizar la función que revisa si hay llaves duplicadas.
    
 END//
 
 
 
 -- Realice un procedimiento para realizar la solicitud de un servicio por parte de un cliente
 
 DELIMITER //
 DROP PROCEDURE IF EXISTS solicitar_servicio //
 CREATE PROCEDURE solicitar_servicio(pFecha DATE, pPuntoPartida POINT, pPuntoLlegada POINT,
 pIdCliente TINYINT, pIdChofer TINYINT, pTipoTransporte TINYINT)
 BEGIN
	DECLARE chofer TINYINT;
	EXPLAIN SELECT ch.idChofer INTO chofer FROM Chofer ch
    INNER JOIN Vehiculo v
    ON ch.idChofer = v.idChofer
    WHERE cd.idChofer = pIdChofer 
    AND (ch.estado != 3 AND ch.estado != 4) AND v.idTipoTransporte = pTipoTransporte;
    
    IF(chofer!= NULL) THEN
		EXPLAIN INSERT INTO Servicio(fecha, puntoPartida, puntoLlegada, idCliente, idChofer)
        VALUES(pFecha, pPuntoPartida, pPuntoLlegada, pIdCliente, chofer);
	END IF;

  --En este procedimiento, por mayor consistencia, se revisa primero si el chofer con el que se quiere hacer el viaje está habilitado, esto para evitar que un chofer que no puede ofrecer servicios debido a una sanción los ofrezca. Si el chofer si está habilitado entonces se inserta un nuevo servicio con ese chofer.
    
 END//
 
 -- Realice un procedimiento que haga el proceso de asignación de puntos a los clientes
 DELIMITER //
 DROP PROCEDURE IF EXISTS asignar_puntos_a_clientes //
 CREATE PROCEDURE asignar_puntos_a_clientes()
 BEGIN
	EXPLAIN UPDATE Cliente c set puntos = 
		(SELECT SUM(r.monto * t.porcentajeXKilometro) AS montoTotal FROM Servicio s, Rango r
        INNER JOIN c
        ON c.idCliente = s.idCliente
        INNER JOIN Chofer ch
        ON s.idChofer = ch.idChofer
        INNER JOIN Vehiculo v
        ON v.idChofer = ch.idChofer
        INNER JOIN TipoTransporte t
        ON v.idTipoTransporte = t.idTipoTransporte
        WHERE (ST_Distance(ST_PointFromText( ST_AsText( s.puntoPartida, s.puntoLlegada ) ) ) 
         )BETWEEN r.inicio AND r.fin);

   --Para este procedure se intentan reducir al máximo, con el uso de inner join, los registros que se deben revisar para hacer la asignación de los puntos. Se hace de esta forma para optmizar el tiempo y la cantidad de registros que deben ser accedidos.
END//

DELIMITER ;

