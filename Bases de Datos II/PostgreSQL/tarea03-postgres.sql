--Instituto Tecnológico de Costa Rica
--Escuela de Ingeniería en Computación
--Curso de Bases de Datos II
--Profesora: Alicia Salazar Hernández
--Tarea 03
--Estudiante: Pedro Henrique Rodríguez de Oliveira (2013086585)
--II Semestre, 2016

--Código hecho para PostgresQL 9.4.

-- Database: tarea

-- DROP DATABASE tarea;

CREATE DATABASE tarea
  --WITH OWNER = pedro
       --ENCODING = 'UTF8'
       --TABLESPACE = pg_default
       --LC_COLLATE = 'pt_BR.UTF-8'
       --LC_CTYPE = 'pt_BR.UTF-8'
       --CONNECTION LIMIT = -1;

CREATE TYPE Electrodomestico AS (
  serial text,
  marca text,
  tipo text,
  precio numeric
);

CREATE TYPE Persona AS (
  nombre text,
  cedula text
);

CREATE TABLE inventario (
  cantidad integer NOT NULL,
  objeto Electrodomestico UNIQUE NOT NULL
);

CREATE TABLE ventas (
  serialFactura text UNIQUE NOT NULL,
  objeto Electrodomestico NOT NULL,
  cliente Persona NOT NULL,
  vendedor Persona NOT NULL,
  fechaDeCompra timestamp NOT NULL
);

CREATE TABLE empleados(
  persona Persona UNIQUE NOT NULL,
  salario numeric NOT NULL
);

CREATE TABLE clientes(
  persona Persona UNIQUE NOT NULL,
  facturas text[] NOT NULL
);

CREATE TABLE pedidos(
  factura text NOT NULL
);
CREATE TABLE envios(
  factura text UNIQUE NOT NULL,
  diaEnvio timestamp NOT NULL,
  diaLlegada timestamp
);


--Parte 1: Consulta e inserción de inventario
--Inserta inventario, haciendo un tipo de upsert (update o insert) si el producto se encuentra o no ahí.
CREATE OR REPLACE FUNCTION insertar_inventario (serial text, marca text, tipo text, precio numeric) RETURNS void AS $$
	DECLARE
		resultado boolean;
	BEGIN
		SELECT EXISTS(SELECT 1 FROM ProductXRack WHERE objeto = ROW(serial, marca, tipo, precio)) INTO resultado;
		IF resultado THEN
			UPDATE inventario SET cantidad = cantidad+1 WHERE objeto = ROW(serial,marca,tipo,precio);
		ELSE
			INSERT INTO inventario (cantidad, objeto) VALUES (1, ROW(serial, marca, tipo, precio));
		END IF;
	END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION consultar_inventario ()
RETURNS TABLE (cantidad integer, objeto electrodomestico) AS $$
	BEGIN
		RETURN QUERY
		SELECT * FROM inventario;
	END;
$$ LANGUAGE 'plpgsql';

--Parte 2: Consulta e inserción de empleados
CREATE OR REPLACE FUNCTION consultar_empleado ()
RETURNS TABLE (persona Persona, salario numeric) AS $$
	BEGIN
		RETURN QUERY
		SELECT * FROM empleados;
	END;
$$ LANGUAGE 'plpgsql'

--Verifica que no se repitan resultados
CREATE OR REPLACE FUNCTION insertar_empleado (nombre text, cedula text, salario numeric)
RETURNS void AS $$
	DECLARE
		resultado boolean;
	BEGIN
		SELECT EXISTS(SELECT 1 FROM empleados WHERE persona=ROW(nombre,cedula)) INTO resultado;
		IF NOT resultado THEN
			INSERT INTO empleados (persona,salario) VALUES (ROW(nombre,cedula), salario);
		END IF;
	END;
$$ LANGUAGE 'plpgsql';

--Parte 3: Ventas
CREATE OR REPLACE FUNCTION venta (aVender Electrodomestico, comprador Persona, vendedor Persona, factura text, envio boolean)
RETURNS void AS $$
	DECLARE
		existe boolean;
	BEGIN
		SELECT EXISTS(SELECT 1 FROM inventario WHERE objeto = aVender AND cantidad <> 0) INTO existe;
		IF existe THEN
			UPDATE inventario SET cantidad = cantidad-1 WHERE objeto = aVender;
			SELECT EXISTS(SELECT 1 FROM clientes WHERE persona = comprador) INTO existe;
			IF NOT existe THEN
				INSERT INTO clientes(persona, facturas) VALUES (comprador, '{}');
			END IF;
			SELECT EXISTS(SELECT 1 FROM empleados WHERE persona = vendedor) INTO existe;
			IF NOT existe THEN
				RAISE EXCEPTION 'Vendedor no existe'
				USING ERRCODE = '36828';
			END IF;
			INSERT INTO ventas VALUES (factura, aVender, comprador, vendedor, current_timestamp);
			UPDATE clientes SET facturas = ARRAY_APPEND(facturas, factura) WHERE persona = comprador;
			IF envio THEN
				INSERT INTO pedidos VALUES (factura);
			END IF;
		ELSE
			RAISE EXCEPTION 'No hay disponibilidad de este producto'
			USING ERRCODE = '34256';
		END IF;
	END;
$$ LANGUAGE 'plpgsql';

--Parte 4: Envíos
CREATE OR REPLACE FUNCTION envio (facturaAEnviar text)
RETURNS void AS $$
	DECLARE
		existePedido boolean;
	BEGIN
		SELECT EXISTS(SELECT 1 FROM pedidos WHERE factura = facturaAEnviar) INTO existePedido;
		IF existePedido THEN
			INSERT INTO envios(factura, diaEnvio) VALUES (facturaAEnviar, current_timestamp);
			DELETE FROM pedidos WHERE factura = facturaAEnviar;
		ELSE
			RAISE EXCEPTION 'Factura no está disponible como pedido'
			USING ERRCODE = '34526';
		END IF;
	END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION llegada (facturaAMArcar text)
RETURNS void AS $$
	DECLARE
		existeEnvio boolean;
	BEGIN
		SELECT EXISTS(SELECT 1 FROM envios WHERE factura = facturaAMArcar) INTO existeEnvio;
		IF existeEnvio THEN
			SELECT EXISTS(SELECT 1 FROM envios WHERE factura = facturaAMArcar AND diallegada IS NULL) INTO existeEnvio;
			IF existeEnvio THEN
				UPDATE envios SET diallegada = current_timestamp WHERE factura = facturaAMArcar;
			ELSE
				RAISE EXCEPTION 'Factura ya ha llegado a cliente'
				USING ERRCODE = '35746';
			END IF;
		ELSE
			RAISE EXCEPTION 'Factura no ha sido enviada'
			USING ERRCODE = '35786';
		END IF;
	END;
$$ LANGUAGE 'plpgsql';

--Parte 5: Consulta más vendidos
CREATE OR REPLACE FUNCTION mas_vendidos(_inicio timestamp, _fin timestamp, _vendedor persona)
RETURNS TABLE(cantidad bigint, objeto Electrodomestico) AS $$
	BEGIN
		RETURN QUERY
		SELECT COUNT(*) AS cantidad, V.objeto FROM ventas V
		WHERE V.fechadecompra >= COALESCE(_inicio,'08/05/2015')
		AND V.fechadecompra < COALESCE(_fin,current_timestamp)
		AND (V.vendedor).nombre LIKE COALESCE((_vendedor).nombre, '%')
		AND (V.vendedor).cedula LIKE COALESCE((_vendedor).cedula, '%')
		GROUP BY V.objeto
		ORDER BY cantidad DESC;
	END;
$$ LANGUAGE 'plpgsql';

--Sección de pruebas
SELECT insertar_inventario ('S344X', 'Mabe', 'Secadora', 35000);
SELECT insertar_inventario ('Y564Y', 'Mabe', 'Lavadora', 35000);
SELECT insertar_inventario ('666ST', 'Mabe', 'Rasuradora', 35000);
SELECT insertar_inventario ('23UY5', 'Mabe', 'Computadora', 35000);
SELECT insertar_inventario ('1234P', 'Mabe', 'Exploradora', 35000);
SELECT insertar_inventario ('453SP', 'Mabe', 'Exploradora', 35000);

SELECT * FROM consultar_inventario();

SELECT insertar_empleado('Juan de los Palotes', '2246541', 45000);
SELECT insertar_empleado('Anita lava la tina', '143674535', 70000);
SELECT insertar_empleado('El marcianito de la cumbia', '9999999', 100000);

SELECT * FROM consultar_empleado();

SELECT * FROM venta (ROW('23UY5', 'Mabe', 'Computadora', 35000), ROW('Andrés Galindo', '4626272'),
				ROW('Juan de los Palotes', '2246541'), '036787', true);

SELECT * FROM clientes;
SELECT * FROM envios;
SELECT * FROM pedidos;
SELECT * FROM ventas;

SELECT * FROM envio ('000004');
SELECT * FROM envio ('0000045');
SELECT * FROM envio ('000006');

SELECT * FROM llegada ('000004');
SELECT * FROM llegada ('0000045');
SELECT * FROM llegada ('000006');

SELECT * FROM mas_vendidos(TIMESTAMP '2016-08-29 21:19:00', localtimestamp, null);
