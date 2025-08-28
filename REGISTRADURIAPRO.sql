create table Departamento(
DepartamentoId int(11) not null,
DepartamentoNombre varchar(32) not null,
PRIMARY KEY(DepartamentoId)
);
create table Ciudad(
CiudadId int(11) not null,
CiudadNombre varchar(32) not null,
DepartamentoId int(11) not null,
PRIMARY KEY(CiudadId),
FOREIGN KEY (DepartamentoId) references Departamento (DepartamentoId)
);
create table Lugarvoto(
LugarId int(11) not null,
DireccionVoto varchar(32) not null,
MesaVoto int(6) not null,
CiudadId int(11) not null,
PRIMARY KEY(LugarId),
FOREIGN KEY (CiudadId) references Ciudad (CiudadId)
);
create table Usuario(
UsuarioId int(11) not null,
Usuario varchar(45) not null,
Password varchar(16) not null,
PRIMARY KEY(UsuarioId)
);
create table Persona(
PersonaId int(12) not null,
PersonaNombre varchar(39) not null,
PersonaApellido varchar(39) not null,
PersonaGenero varchar(1) not null,
PersonaFechaN DATE not null,
PersonaJurado int(1) not null,
LugarId int(11) not null,
UsuarioId int(11) not null,
PRIMARY KEY(PersonaId),
FOREIGN KEY (LugarId) references Lugarvoto (LugarId),
FOREIGN KEY (UsuarioId) references Usuario (UsuarioId)
);
create table Registro(
RegistrosId int(11) not null,
DocId int(11) not null,
PersonaId int(12) not null,
PRIMARY KEY(RegistrosId),
FOREIGN KEY (PersonaId) references Persona (PersonaId)
);
