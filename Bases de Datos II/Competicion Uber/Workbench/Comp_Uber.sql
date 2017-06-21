-- MySQL Script generated by MySQL Workbench
-- Fri 28 Oct 2016 04:55:51 PM CST
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

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
