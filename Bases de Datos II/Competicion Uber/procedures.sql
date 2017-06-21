
-- Realice un procedimiento que obtenga los choferes que hay que llamarles 
-- la atención o que haya que suspender o eliminar de la bd de proveedores

DELIMITER //
DROP PROCEDURE IF EXISTS consultar_choferes_amonestados //
CREATE PROCEDURE consultar_choferes_amonestados()
BEGIN
	SELECT ch.nombre, ch.primerApellido, ch.segundoApellido, CalificacionTotal 
    FROM Chofer ch INNER JOIN Calificacion ca
    ON ch.idChofer = ca.idChofer
    WHERE (SELECT AVG(ca.calificacion) AS CalificacionTotal FROM ca 
    WHERE ca.idChofer = ch.idChofer) <= 3.0;

	SELECT ch.nombre,ch.primerApellido, ch.segundoApellido
    FROM Chofer ch INNER JOIN Calificacion ca
    ON ch.idChofer = ca.idChofer
    WHERE(SELECT AVG(ca.calificacion) FROM ca
    INNER JOIN Servicio s
    ON ca.idServicio = s.idServicio
    WHERE ca.idChofer = ch.idChofer AND 
    (SELECT TIMESTAMPDIFF(MONTH, CURDATE(), s.fecha) ) >= 2 
    ) <= 3.0;
    
    SELECT ch.nombre, ch.primerApellido, ch.segundoApellido, CalificacionTotal FROM Chofer ch
    INNER JOIN Calificacion ca
    ON ch.idChofer = ca.idChofer
	WHERE ch.idEstado = 4 AND (SELECT AVG(ca.calificacion) AS CalificacionTotal FROM ca 
    WHERE ca.idChofer = ch.idChofer) <= 3.0;
    
END//

-- Realice un procedimiento para hacer ingreso, actualización de clientes

DELIMITER //
DROP PROCEDURE IF EXISTS insertar_actualizar_cliente //
CREATE PROCEDURE insertar_actualizar_cliente(pIdCliente TINYINT,pNombre VARCHAR(25), pPrimerApellido VARCHAR(25),
 pSegundoApellido VARCHAR(25) )
 BEGIN
	INSERT INTO Cliente(idCliente, nombre, primerApellido, segundoApellido)
    VALUES(pIdCliente, pNombre, pPrimerApellido, pSegundoApellido)
    ON DUPLICATE KEY UPDATE nombre = pNombre, primerApellido = pPrimerApellido, 
    segundoApellido = pSegundoApellido;
    
 END//
 
 
 
 -- Realice un procedimiento para realizar la solicitud de un servicio por parte de un cliente
 
 DELIMITER //
 DROP PROCEDURE IF EXISTS solicitar_servicio //
 CREATE PROCEDURE solicitar_servicio(pFecha DATE, pPuntoPartida POINT, pPuntoLlegada POINT,
 pIdCliente TINYINT, pIdChofer TINYINT, pTipoTransporte TINYINT)
 BEGIN
	DECLARE chofer TINYINT;
	SELECT ch.idChofer INTO chofer FROM Chofer ch
    INNER JOIN Vehiculo v
    ON ch.idChofer = v.idChofer
    WHERE cd.idChofer = pIdChofer 
    AND (ch.estado != 3 AND ch.estado != 4) AND v.idTipoTransporte = pTipoTransporte;
    
    IF(chofer!= NULL) THEN
		INSERT INTO Servicio(fecha, puntoPartida, puntoLlegada, idCliente, idChofer)
        VALUES(pFecha, pPuntoPartida, pPuntoLlegada, pIdCliente, chofer);
	END IF;
    
 END//
 
 -- Realice un procedimiento que haga el proceso de asignación de puntos a los clientes
 DELIMITER //
 DROP PROCEDURE IF EXISTS asignar_puntos_a_clientes //
 CREATE PROCEDURE asignar_puntos_a_clientes()
 BEGIN
	UPDATE Cliente c set puntos = 
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
END//
 
 
 
 