
from django.db import models

class Departamento(models.Model):
	DepartamentoId = models.AutoField(primary_key=True)
	DepartamentoNombre = models.CharField(max_length=32)

	def __str__(self):
		return self.DepartamentoNombre

class Ciudad(models.Model):
	CiudadId = models.AutoField(primary_key=True)
	CiudadNombre = models.CharField(max_length=32)
	Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

	def __str__(self):
		return self.CiudadNombre

class Lugarvoto(models.Model):
	LugarId = models.AutoField(primary_key=True)
	DireccionVoto = models.CharField(max_length=32)
	MesaVoto = models.IntegerField()
	Ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.DireccionVoto} - Mesa {self.MesaVoto}"

class Usuario(models.Model):
	UsuarioId = models.AutoField(primary_key=True)
	Usuario = models.CharField(max_length=45)
	Password = models.CharField(max_length=16)

	def __str__(self):
		return self.Usuario

class Persona(models.Model):
	PersonaId = models.AutoField(primary_key=True)
	PersonaNombre = models.CharField(max_length=39)
	PersonaApellido = models.CharField(max_length=39)
	PersonaGenero = models.CharField(max_length=1)
	PersonaFechaN = models.DateField()
	PersonaJurado = models.BooleanField()
	Lugar = models.ForeignKey(Lugarvoto, on_delete=models.CASCADE)
	Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.PersonaNombre} {self.PersonaApellido}"

class Registro(models.Model):
	RegistrosId = models.AutoField(primary_key=True)
	DocId = models.IntegerField()
	Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

	def __str__(self):
		return f"Registro {self.RegistrosId} - Persona {self.Persona_id}"
