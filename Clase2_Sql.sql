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





