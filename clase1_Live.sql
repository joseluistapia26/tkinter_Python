create database lives_sql;
use lives_sql;
create table estudiantes(
    id int auto_increment,
    cedula varchar(10) not null,
    nombres varchar(50) not null,
    apellidos varchar(50) not null,
    fecha_nacimiento date,
    estado varchar(1) not null,
    primary key (id),
    unique (cedula)
);
select * from estudiantes;
insert into  estudiantes(cedula,nombres,apellidos,
fecha_nacimiento,estado) values('0987654321','CARLOS LUIS',
'VERA MORALES','1980-05-12','A');
insert into estudiantes(cedula,nombres,apellidos,fecha_nacimiento,
estado) values('0123454321','JORGE LUIS',
'MORA PEREZ','1990-08-09','A');

select nombres,apellidos,fecha_nacimiento
from estudiantes;

