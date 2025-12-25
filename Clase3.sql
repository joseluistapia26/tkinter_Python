Canal: https://www.youtube.com/watch?v=fZ55J4WhdIo&t=3s



-- script de calculo
CREATE TABLE ventas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    cantidad INT NOT NULL,
    total DECIMAL(10,2) AS (precio * cantidad) STORED
);

INSERT INTO ventas (producto, precio, cantidad) VALUES
('Producto A', 10.00, 2),
('Producto B', 15.50, 1),
('Producto C', 7.25, 5),
('Producto D', 20.00, 3),
('Producto E', 5.75, 4);
select * from ventas;

CREATE TABLE ventas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    cantidad INT NOT NULL,
    total DECIMAL(10,2) NOT NULL DEFAULT 0
);

INSERT INTO ventas (producto, precio, cantidad) VALUES
('Producto A', 10.00, 2),
('Producto B', 15.50, 1),
('Producto C', 7.25, 5),
('Producto D', 20.00, 3),
('Producto E', 5.75, 4);
SET SQL_SAFE_UPDATES = 0;
UPDATE ventas
SET total = precio * cantidad;
select * from ventas;

DELIMITER $$
create view vista_ventas as
select
 id, producto, precio, cantidad,
 total
 from ventas
 DELIMITER;
select * from vista_ventas;



-- crear una tabla ventas con id, producto, cantidad, precio,
-- total
CREATE TABLE ventas2 (
    id SERIAL PRIMARY KEY,
    producto VARCHAR(100) NOT NULL,
    cantidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    total DECIMAL(10, 2) not null default 0
);
-- insertar 10 registros en la tabla ventas

-- TRIGGER
DELIMITER $$
create trigger tr1_ventas2
before insert on ventas2
for each row
begin
     set NEW.total = NEW.precio * NEW.cantidad;
end$$
DELIMITER ;

CREATE TABLE ventas2 (
    id SERIAL PRIMARY KEY,
    producto VARCHAR(100) NOT NULL,
    cantidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    total DECIMAL(10, 2) not null default 0
);
-- insertar 10 registros en la tabla ventas
INSERT INTO ventas2 (producto, cantidad, precio) VALUES
('Producto A', 2, 10.00),
('Producto B', 1, 20.00),
('Producto C', 5, 5.00),
('Producto D', 3, 15.00),
('Producto E', 4, 8.00),
('Producto F', 6, 12.00),
('Producto G', 2, 25.00),
('Producto H', 7, 7.00),
('Producto I', 1, 30.00),
('Producto J', 8, 4.00);

select * from ventas2;



