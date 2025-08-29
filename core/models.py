from django.db import models


class Departamento(models.Model):
	"""
	Modelo que representa un departamento administrativo.
	"""
	cod_Departamento = models.CharField(max_length=255, primary_key=True)
	departamento = models.CharField(max_length=255)

	def __str__(self):
		return self.departamento


class Ciudad(models.Model):
	"""
	Modelo que representa una ciudad, asociada a un departamento.
	"""
	cod_Ciudad = models.CharField(max_length=255, primary_key=True)
	ciudad = models.CharField(max_length=255)
	cod_Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, db_column='cod_Departamento')

	def __str__(self):
		return self.ciudad


class Lugar(models.Model):
	"""
	Modelo que representa un lugar de votación, asociado a una ciudad.
	"""
	cod_lugar = models.CharField(max_length=255, primary_key=True)
	nombre_lugar = models.CharField(max_length=255)
	direccion = models.CharField(max_length=255)
	cod_Ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, db_column='cod_Ciudad')

	def __str__(self):
		return f"{self.nombre_lugar} - {self.direccion}"

class Mesa(models.Model):
	cod_Mesa = models.BigAutoField(primary_key=True)
	mesa = models.IntegerField()
	cod_lugar = models.ForeignKey('Lugar', on_delete=models.CASCADE, db_column='cod_lugar')

	def __str__(self):
		return f"Mesa {self.mesa} ({self.cod_Mesa})"

class Usuario(models.Model):
	"""
	Modelo que representa un usuario del sistema.
	"""

	def __str__(self):
		return self.Usuario


class Persona(models.Model):
	"""
	Modelo que representa una persona registrada para votar.
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
	Modelo que representa el registro de una persona (por ejemplo, su cédula).
	"""
	cod_Registro = models.BigAutoField(primary_key=True)
	registro = models.IntegerField()
	cedula = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='cedula')

	def __str__(self):
		return f"Registro {self.cod_Registro} - Persona {self.cedula_id}"
