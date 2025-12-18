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

-- clase 2
select nombres,apellidos,fecha_nacimiento
from estudiantes;
insert into estudiantes(cedula,nombres,apellidos,fecha_nacimiento,
estado) values 
('1234567890','ALBERTO RICARDO','MENENDEZ FABRE','1984-03-12','A'),
('0987612345','MARIA ALEJANDRA','SOTO RUIZ','1970-01-31','A'),
('1234565678','ANGELO OSCAR','PULIDO LOPEZ','1991-09-19','A'),
('1134612345','JEAN PAUL','VARGAS CORONEL','1980-12-31','A'),
('0223612345','CAMILO EDISON','CASTRO PEREZ','1975-07-16','A');

SELECT * FROM ESTUDIANTES;

SELECT * FROM estudiantes;
select nombres as NOMBRES, apellidos as APELLIDOS
from estudiantes;

select * from estudiantes where id>3 and id<7;
select * from estudiantes order by apellidos;
select * from estudiantes order by nombres;
select * from estudiantes order by fecha_nacimiento;

select * from estudiantes 
where apellidos like 'V%'

select count(*) as Total from estudiantes;
select * from estudiantes where cedula='0987612345';

select * from estudiantes 
where nombres like '%an%';

select * from estudiantes
where apellidos like '%PEREZ%';

SELECT * FROM estudiantes
where fecha_nacimiento between '1980-01-01' and
'1991-01-01';

