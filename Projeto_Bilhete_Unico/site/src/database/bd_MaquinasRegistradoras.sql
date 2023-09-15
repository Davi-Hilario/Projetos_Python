create database bd_AnaliseMaquinasRegistradoras;
use bd_AnaliseMaquinasRegistradoras;

create table Maquina
(
	idMaquina int primary key auto_increment,
    nomeMaquina varchar(20)
);

create table Registro
(
	idRegistro int primary key auto_increment,
	cpu_percent decimal(4,1),
	memoria_percent decimal(4,1),
	disco_percent decimal(4,1),
    dataRegistro datetime,
    fkMaquina int,
    foreign key(fkMaquina) references Maquina(idMaquina)
);

insert into maquina values
(null, 'Maquina 1'),
(null, 'Maquina 2'),
(null, 'Maquina 3');

select * from registro;

