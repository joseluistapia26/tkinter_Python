CREATE DATABASE IF NOT EXISTS `lives_mysql` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `lives_mysql`;

-- ESTRUCTURA DE TABLAS

CREATE TABLE `categorias` (
  `id_categoria` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  `estado` varchar(1) NOT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `articulos` (
  `id_articulo` int NOT NULL AUTO_INCREMENT,
  `id_categoria` int NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `estado` varchar(1) NOT NULL,
  PRIMARY KEY (`id_articulo`),
  KEY `id_categoria` (`id_categoria`),
  CONSTRAINT `articulos_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id_categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `marcas` (
  `id_marca` int NOT NULL AUTO_INCREMENT,
  `id_articulo` int NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `estado` varchar(1) NOT NULL,
  PRIMARY KEY (`id_marca`),
  KEY `id_articulo` (`id_articulo`),
  CONSTRAINT `marcas_ibfk_1` FOREIGN KEY (`id_articulo`) REFERENCES `articulos` (`id_articulo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `productos` (
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `id_marca` int NOT NULL,
  `codigo` varchar(30) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `stock` int NOT NULL DEFAULT '0',
  `estado` varchar(1) NOT NULL,
  PRIMARY KEY (`id_producto`),
  KEY `id_marca` (`id_marca`),
  CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`id_marca`) REFERENCES `marcas` (`id_marca`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `ventas` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `producto` varchar(100) NOT NULL,
  `cantidad` int NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `total` decimal(10,2) GENERATED ALWAYS AS ((`cantidad` * `precio`)) STORED,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `ventas2` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `producto` varchar(100) NOT NULL,
  `cantidad` int NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `total` decimal(10,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- INSERCIÓN DE DATOS

INSERT INTO `categorias` (`id_categoria`, `nombre`, `estado`) VALUES 
(1,'COMPUTACION','A'), (2,'REDES','A'), (3,'ALIMENTOS','A'), (4,'MEDICINA','A');

INSERT INTO `articulos` (`id_articulo`, `id_categoria`, `nombre`, `estado`) VALUES 
(1,1,'LAPTOP','A'), (2,1,'MOUSE','A'), (3,2,'ROUTER','A'), (4,3,'ACEITE VEGETAL','A'), (5,3,'ATUN','A'), (6,4,'JARABE','A');

INSERT INTO `marcas` (`id_marca`, `id_articulo`, `nombre`, `estado`) VALUES 
(1,1,'LENOVO','A'), (2,1,'APPLE','A'), (3,2,'GENIUS','A'), (4,3,'t LINK','A'), (5,4,'GIRASOL','A'), (6,5,'ISABEL','A'), (7,6,'ABBOT','A');

INSERT INTO `productos` (`id_producto`, `id_marca`, `codigo`, `nombre`, `precio`, `stock`, `estado`) VALUES 
(1,1,'LP01','THINKPAD E14 GEN 5',1000.00,10,'A'), (2,3,'MS01','MOUSE M185',10.00,15,'A'), (3,4,'RT01','ARCHER AX10',30.00,20,'A'), 
(4,5,'AC01','GIRASOL CERO GRASA',3.00,25,'A'), (5,6,'AT01','LOMITOS ENTEROS',2.50,60,'A'), (6,7,'JR01','ANTI TOS',3.75,30,'A');

INSERT INTO `ventas` (`id`, `producto`, `cantidad`, `precio`) VALUES 
(1,'Producto A',2,10.00), (2,'Producto B',1,20.00), (3,'Producto C',5,5.00), (4,'Producto D',3,15.00), (5,'Producto E',4,8.00), 
(6,'Producto F',6,12.00), (7,'Producto G',2,25.00), (8,'Producto H',7,7.00), (9,'Producto I',1,30.00), (10,'Producto J',8,4.00),
(11,'Producto A',2,10.00), (12,'Producto B',1,20.00), (13,'Producto C',5,5.00), (14,'Producto D',3,15.00), (15,'Producto E',4,8.00), 
(16,'Producto F',6,12.00), (17,'Producto G',2,25.00), (18,'Producto H',7,7.00), (19,'Producto I',1,30.00), (20,'Producto J',8,4.00);

INSERT INTO `ventas2` VALUES 
(1,'Producto A',2,10.00,20.00), (2,'Producto B',1,20.00,20.00), (3,'Producto C',5,5.00,25.00), (4,'Producto D',3,15.00,45.00), 
(5,'Producto E',4,8.00,32.00), (6,'Producto F',6,12.00,72.00), (7,'Producto G',2,25.00,50.00), (8,'Producto H',7,7.00,49.00), 
(9,'Producto I',1,30.00,30.00), (10,'Producto J',8,4.00,32.00);

-- VISTAS

CREATE VIEW `vista_ventas` AS 
SELECT `id`, `producto`, `precio`, `cantidad`, `total` 
FROM `ventas`;

-- PROCEDIMIENTOS ALMACENADOS

DELIMITER ;;

CREATE PROCEDURE `getMessage`(in promedio double, out mensaje text)
BEGIN
    if promedio>=7 and promedio<=10 then set mensaje='APROBADO'; end if;
    if promedio>=0 and promedio<7 then set mensaje='REPROBADO'; end if;
    if promedio<0 or promedio>10 then set mensaje = 'VALOR INVALIDO!'; end if;
END ;;

CREATE PROCEDURE `getPromedio`(in n1 double, in n2 double, in n3 double, out resultado double)
BEGIN
    set resultado = (n1+n2+n3)/3;
END ;;

CREATE PROCEDURE `procedimiento1`(in saludo text, out cadena text)
BEGIN
    set cadena = 'Hola mundo';
END ;;

CREATE PROCEDURE `promedio`(in nota1 double, in nota2 double, in nota3 double, out promedio double, out mensaje text)
BEGIN
    call getPromedio(nota1, nota2, nota2, promedio);
    call getMessage(promedio, mensaje);
END ;;

DELIMITER ;


