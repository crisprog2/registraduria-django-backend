from django.db import models


class Departamento(models.Model):
	"""
	Modelo de Departamento.
	Representa un departamento administrativo de Colombia.

	Campos:
		cod_Departamento (CharField): Código único del departamento (PK).
		departamento (CharField): Nombre del departamento.
	"""
	cod_Departamento = models.CharField(max_length=255, primary_key=True)
	departamento = models.CharField(max_length=255)

	def __str__(self):
		return self.departamento


class Ciudad(models.Model):
	"""
	Modelo de Ciudad.
	Representa una ciudad asociada a un departamento.

	Campos:
		cod_Ciudad (CharField): Código único de la ciudad (PK).
		ciudad (CharField): Nombre de la ciudad.
		cod_Departamento (ForeignKey): Departamento al que pertenece la ciudad.
	"""
	cod_Ciudad = models.CharField(max_length=255, primary_key=True)
	ciudad = models.CharField(max_length=255)
	cod_Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, db_column='cod_Departamento')

	def __str__(self):
		return self.ciudad


class Lugar(models.Model):
	"""
	Modelo de Lugar de Votación.
	Representa un lugar físico donde se vota, asociado a una ciudad.

	Campos:
		cod_lugar (CharField): Código único del lugar (PK).
		nombre_lugar (CharField): Nombre del lugar.
		direccion (CharField): Dirección física.
		cod_Ciudad (ForeignKey): Ciudad a la que pertenece el lugar.
	"""
	cod_lugar = models.CharField(max_length=255, primary_key=True)
	nombre_lugar = models.CharField(max_length=255)
	direccion = models.CharField(max_length=255)
	cod_Ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, db_column='cod_Ciudad')

	def __str__(self):
		return f"{self.nombre_lugar} - {self.direccion}"

class Mesa(models.Model):
	"""
	Modelo de Mesa de Votación.
	Representa una mesa dentro de un lugar de votación.

	Campos:
		cod_Mesa (BigAutoField): ID único de la mesa (PK).
		mesa (IntegerField): Número de la mesa.
		cod_lugar (ForeignKey): Lugar de votación al que pertenece la mesa.
	"""
	cod_Mesa = models.BigAutoField(primary_key=True)
	mesa = models.IntegerField()
	cod_lugar = models.ForeignKey('Lugar', on_delete=models.CASCADE, db_column='cod_lugar')

	def __str__(self):
		return f"Mesa {self.mesa} ({self.cod_Mesa})"

class Usuario(models.Model):
	"""
	Modelo de Usuario (actualmente no utilizado).
	Reservado para futuras implementaciones de autenticación.
	"""

	def __str__(self):
		return self.Usuario


class Persona(models.Model):
	"""
	Modelo de Persona.
	Representa a una persona registrada para votar.

	Campos:
		cedula (IntegerField): Número de cédula (PK).
		primer_Nombre, segundo_Nombre, primer_Apellido, segundo_Apellido (CharField): Nombres y apellidos.
		genero (CharField): Género de la persona.
		edad (IntegerField): Edad de la persona.
		jurado (CharField): Indica si es jurado de votación.
		cod_Mesa (ForeignKey): Mesa de votación asignada.
	"""
	cedula = models.IntegerField(primary_key=True)
	primer_Nombre = models.CharField(max_length=255)
	segundo_Nombre = models.CharField(max_length=255)
	primer_Apellido = models.CharField(max_length=255)
	segundo_Apellido = models.CharField(max_length=255)
	genero = models.CharField(max_length=50)
	edad = models.IntegerField()
	jurado = models.CharField(max_length=50)
	cod_Mesa = models.ForeignKey('Mesa', on_delete=models.CASCADE, db_column='cod_Mesa')
	# Relación con Usuario eliminada

	def __str__(self):
		return f"{self.primer_Nombre} {self.primer_Apellido}"


class Registro(models.Model):
	"""
	Modelo de Registro.
	Representa el registro de una persona (por ejemplo, su inscripción electoral o consulta).

	Campos:
		cod_Registro (BigAutoField): ID único del registro (PK).
		registro (IntegerField): Número de registros/consultas.
		cedula (ForeignKey): Persona asociada al registro.
	"""
	cod_Registro = models.BigAutoField(primary_key=True)
	registro = models.IntegerField()
	cedula = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='cedula')

	def __str__(self):
		return f"Registro {self.cod_Registro} - Persona {self.cedula_id}"
