-- Script de creación de tablas para el sistema de registraduría

CREATE TABLE tabla_departamento (
    cod_Departamento VARCHAR(255) PRIMARY KEY,
    departamento VARCHAR(255)
);

CREATE TABLE tabla_ciudad (
    cod_Ciudad VARCHAR(255) PRIMARY KEY,
    ciudad VARCHAR(255),
    cod_Departamento VARCHAR(255),
    FOREIGN KEY (cod_Departamento) REFERENCES tabla_departamento(cod_Departamento)
);

CREATE TABLE tabla_lugar (
    cod_lugar VARCHAR(255) PRIMARY KEY,
    nombre_lugar VARCHAR(255),
    direccion VARCHAR(255),
    cod_Ciudad VARCHAR(255),
    FOREIGN KEY (cod_Ciudad) REFERENCES tabla_ciudad(cod_Ciudad)
);

CREATE TABLE tabla_mesa (
    cod_Mesa BIGINT PRIMARY KEY AUTO_INCREMENT,
    mesa INT,
    cod_lugar VARCHAR(255),
    FOREIGN KEY (cod_lugar) REFERENCES tabla_lugar(cod_lugar)
);

CREATE TABLE tabla_persona (
    cedula INT PRIMARY KEY,
    primer_Nombre VARCHAR(255),
    segundo_Nombre VARCHAR(255),
    primer_Apellido VARCHAR(255),
    segundo_Apellido VARCHAR(255),
    genero VARCHAR(50),
    edad INT,
    jurado VARCHAR(50),
    cod_Mesa BIGINT,
    FOREIGN KEY (cod_Mesa) REFERENCES tabla_mesa(cod_Mesa)
);

CREATE TABLE tabla_registro (
    cod_Registro BIGINT PRIMARY KEY AUTO_INCREMENT,
    registro INT,
    cedula INT NOT NULL,
    FOREIGN KEY (cedula) REFERENCES tabla_persona(cedula)
);
