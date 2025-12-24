create database lives_mysql;
use lives_mysql;
create table categorias(
    id_categoria int auto_increment primary key,
    nombre varchar(20) not null,
    estado varchar(1) not null
);

create table articulos(
    id_articulo int auto_increment primary key,
    id_categoria int not null, -- va a ser clave foranea 
    nombre varchar(25) not null,
    estado varchar(1) not null
);

create table marcas(
	id_marca int auto_increment primary key,
    id_articulo int not null, -- va  a ser clave foranea
    nombre varchar(25) not null,
    estado varchar(1) not null
);


create table productos(
     id_producto int auto_increment primary key,
     id_marca int not null,
     codigo varchar(30) not null,
     nombre varchar(50) not null,
     precio decimal(10,2) not null,
     stock int not null default 0,
     estado varchar(1) not null
);

-- relaciones

alter table articulos
add foreign key (id_categoria)
references categorias(id_categoria);

alter table marcas
add foreign key (id_articulo)
references articulos(id_articulo);

alter table productos
add foreign key (id_marca)
references marcas(id_marca);

-- inserts - join
create database lives_mysql;
use lives_mysql;
create table categorias(
    id_categoria int auto_increment primary key,
    nombre varchar(20) not null,
    estado varchar(1) not null
);

create table articulos(
    id_articulo int auto_increment primary key,
    id_categoria int not null, -- va a ser clave foranea 
    nombre varchar(25) not null,
    estado varchar(1) not null
);

create table marcas(
	id_marca int auto_increment primary key,
    id_articulo int not null, -- va  a ser clave foranea
    nombre varchar(25) not null,
    estado varchar(1) not null
);


create table productos(
     id_producto int auto_increment primary key,
     id_marca int not null,
     codigo varchar(30) not null,
     nombre varchar(50) not null,
     precio decimal(10,2) not null,
     stock int not null default 0,
     estado varchar(1) not null
);

-- relaciones

alter table articulos
add foreign key (id_categoria)
references categorias(id_categoria);

alter table marcas
add foreign key (id_articulo)
references articulos(id_articulo);

alter table productos
add foreign key (id_marca)
references marcas(id_marca);

-- INSERT
insert into categorias(nombre,estado)
values ('COMPUTACION','A'),
('REDES','A') ,
('ALIMENTOS','A'),
('MEDICINA','A');

select * from categorias;

insert into articulos (id_categoria,nombre,estado)
values (1,'LAPTOP','A'),
 (1,'MOUSE','A'),
 (2,'ROUTER','A'),
 (3,'ACEITE VEGETAL','A'),
 (3,'ATUN','A'),
 (4,'JARABE','A');
 
 select * from articulos;
 
 insert into marcas(id_articulo,nombre,estado)
 values (1,'LENOVO','A'),
      (1,'APPLE','A'),
      (2,'GENIUS','A'),
      (3,'t LINK','A'),
      (4,'GIRASOL','A'),
      (5,'ISABEL','A'),
      (6,'ABBOT','A');
SELECT  * FROM marcas;

insert into productos (id_marca,codigo,nombre,precio,stock,
           estado)
values (1,'LP01','THINKPAD E14 GEN 5',1000,10,'A'),
       (3,'MS01','MOUSE M185',10,15,'A'),
       (4,'RT01','ARCHER  AX10',30,20,'A'),
       (5,'AC01','GIRASOL CERO GRASA',3,25,'A'),
       (6,'AT01','LOMITOS ENTEROS',2.50,60,'A'),
       (7,'JR01','ANTI TOS',3.75,30,'A');
                    
select * from productos;
use lives_mysql;
select a.id_articulo,c.nombre as CATEGORIA, 
a.nombre AS ARTICULO
from categorias c, articulos a
where a.id_categoria=c.id_categoria;

select  a.nombre as Articulo, m.nombre as Marca
  from articulos a , marcas m
where m.id_articulo= a.id_articulo;

select m.nombre as MARCA,p.nombre as PRODUCTO,
p.codigo, p.precio,p.stock
 from marcas m, productos p
where p.id_marca=m.id_marca;

--  consulta Ejercicios con Joins 8:35pm
select 
p.id_producto,c.nombre AS CATEGORIA, a.nombre AS ARTICULO,
  m.nombre AS MARCA, p.codigo, p.nombre AS PRODUCTO,
  p.precio, p.stock
from categorias c, articulos a, marcas m,productos p
where p.id_marca= m.id_marca
and   m.id_articulo= a.id_articulo
and   a.id_categoria = c.id_categoria

-- INNER JOIN

select p.nombre as PRODUCTO, m.nombre as MARCA
from productos p
Inner join marcas m on p.id_marca= m.id_marca;

-- LEFT JOIN

select p.nombre as PRODUCTO, m.nombre as MARCA
from productos p
LEFT join marcas m on p.id_marca= m.id_marca;

-- Consula todo palabras Joins
select 
p.id_producto,c.nombre AS CATEGORIA, a.nombre AS ARTICULO,
  m.nombre AS MARCA, p.codigo, p.nombre AS PRODUCTO,
  p.precio, p.stock
from productos p
Inner join marcas m on p.id_marca=m.id_marca
left join articulos a on m.id_articulo= a.id_articulo
left join categorias c on   a.id_categoria = c.id_categoria  ;






