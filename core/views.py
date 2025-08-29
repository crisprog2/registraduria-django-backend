# --- Ciudad ---
"""
Endpoints para Ciudad:
- GET /api/ciudades/ : Lista todas las ciudades
- POST /api/ciudades/ : Crea una nueva ciudad
- GET /api/ciudades/<id>/ : Consulta una ciudad por ID
- PUT /api/ciudades/<id>/ : Actualiza una ciudad
- DELETE /api/ciudades/<id>/ : Elimina una ciudad
"""
# --- Lugarvoto ---
"""
Endpoints para Lugarvoto:
- GET /api/lugaresvoto/ : Lista todos los lugares de voto
- POST /api/lugaresvoto/ : Crea un nuevo lugar de voto
- GET /api/lugaresvoto/<id>/ : Consulta un lugar de voto por ID
- PUT /api/lugaresvoto/<id>/ : Actualiza un lugar de voto
- DELETE /api/lugaresvoto/<id>/ : Elimina un lugar de voto
"""
# --- Persona ---
"""
Endpoints para Persona:
- GET /api/personas/ : Lista todas las personas
- POST /api/personas/ : Crea una nueva persona
- GET /api/personas/<id>/ : Consulta una persona por ID
- PUT /api/personas/<id>/ : Actualiza una persona
- DELETE /api/personas/<id>/ : Elimina una persona
"""
# --- Registro ---
"""
Endpoints para Registro:
- GET /api/registros/ : Lista todos los registros
- POST /api/registros/ : Crea un nuevo registro
- GET /api/registros/<id>/ : Consulta un registro por ID
- PUT /api/registros/<id>/ : Actualiza un registro
- DELETE /api/registros/<id>/ : Elimina un registro
"""
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, Http404
from django.views.decorators.http import require_http_methods
import json
from .models import Departamento, Ciudad, Lugarvoto, Persona, Registro
# --- Ciudad ---
@require_http_methods(["GET", "POST"])
@csrf_exempt
def ciudades_list(request):
	if request.method == "GET":
		ciudades = Ciudad.objects.all().values('CiudadId', 'CiudadNombre', 'Departamento_id')
		return JsonResponse(list(ciudades), safe=False)
	elif request.method == "POST":
		try:
			data = json.loads(request.body)
			nombre = data.get('CiudadNombre')
			departamento_id = data.get('Departamento')
			if not nombre or not departamento_id:
				return JsonResponse({'error': 'CiudadNombre y Departamento son requeridos'}, status=400)
			ciudad = Ciudad.objects.create(CiudadNombre=nombre, Departamento_id=departamento_id)
			return JsonResponse({'CiudadId': ciudad.CiudadId, 'CiudadNombre': ciudad.CiudadNombre, 'Departamento': ciudad.Departamento_id}, status=201)
		except Exception as e:
			return JsonResponse({'error': str(e)}, status=400)
	else:
		return HttpResponseNotAllowed(['GET', 'POST'])

@require_http_methods(["GET", "PUT", "DELETE"])
@csrf_exempt
def ciudad_detail(request, id):
	try:
		ciudad = Ciudad.objects.get(CiudadId=id)
	except Ciudad.DoesNotExist:
		return JsonResponse({'error': 'No existe la ciudad'}, status=404)

	if request.method == "GET":
		return JsonResponse({'CiudadId': ciudad.CiudadId, 'CiudadNombre': ciudad.CiudadNombre, 'Departamento': ciudad.Departamento_id})
	elif request.method == "PUT":
		try:
			data = json.loads(request.body)
			nombre = data.get('CiudadNombre')
			departamento_id = data.get('Departamento')
			if not nombre or not departamento_id:
				return JsonResponse({'error': 'CiudadNombre y Departamento son requeridos'}, status=400)
			ciudad.CiudadNombre = nombre
			ciudad.Departamento_id = departamento_id
			ciudad.save()
			return JsonResponse({'CiudadId': ciudad.CiudadId, 'CiudadNombre': ciudad.CiudadNombre, 'Departamento': ciudad.Departamento_id})
		except Exception as e:
			return JsonResponse({'error': str(e)}, status=400)
	elif request.method == "DELETE":
		ciudad.delete()
		return HttpResponse(status=204)
	else:
		return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])

# --- Lugarvoto ---
@require_http_methods(["GET", "POST"])
@csrf_exempt
def lugaresvoto_list(request):
	if request.method == "GET":
		lugares = Lugarvoto.objects.all().values('LugarId', 'DireccionVoto', 'MesaVoto', 'Ciudad_id')
		return JsonResponse(list(lugares), safe=False)
	elif request.method == "POST":
		try:
			data = json.loads(request.body)
			direccion = data.get('DireccionVoto')
			mesa = data.get('MesaVoto')
			ciudad_id = data.get('Ciudad')
			if not direccion or mesa is None or not ciudad_id:
				return JsonResponse({'error': 'DireccionVoto, MesaVoto y Ciudad son requeridos'}, status=400)
			lugar = Lugarvoto.objects.create(DireccionVoto=direccion, MesaVoto=mesa, Ciudad_id=ciudad_id)
			return JsonResponse({'LugarId': lugar.LugarId, 'DireccionVoto': lugar.DireccionVoto, 'MesaVoto': lugar.MesaVoto, 'Ciudad': lugar.Ciudad_id}, status=201)
		except Exception as e:
			return JsonResponse({'error': str(e)}, status=400)
	else:
		return HttpResponseNotAllowed(['GET', 'POST'])

@require_http_methods(["GET", "PUT", "DELETE"])
@csrf_exempt
def lugarvoto_detail(request, id):
	try:
		lugar = Lugarvoto.objects.get(LugarId=id)
	except Lugarvoto.DoesNotExist:
		return JsonResponse({'error': 'No existe el lugar de voto'}, status=404)

	if request.method == "GET":
		return JsonResponse({'LugarId': lugar.LugarId, 'DireccionVoto': lugar.DireccionVoto, 'MesaVoto': lugar.MesaVoto, 'Ciudad': lugar.Ciudad_id})
	elif request.method == "PUT":
		try:
			data = json.loads(request.body)
			direccion = data.get('DireccionVoto')
			mesa = data.get('MesaVoto')
			ciudad_id = data.get('Ciudad')
			if not direccion or mesa is None or not ciudad_id:
				return JsonResponse({'error': 'DireccionVoto, MesaVoto y Ciudad son requeridos'}, status=400)
			lugar.DireccionVoto = direccion
			lugar.MesaVoto = mesa
			lugar.Ciudad_id = ciudad_id
			lugar.save()
			return JsonResponse({'LugarId': lugar.LugarId, 'DireccionVoto': lugar.DireccionVoto, 'MesaVoto': lugar.MesaVoto, 'Ciudad': lugar.Ciudad_id})
		except Exception as e:
			return JsonResponse({'error': str(e)}, status=400)
	elif request.method == "DELETE":
		lugar.delete()
		return HttpResponse(status=204)
	else:
		return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])

# --- Persona ---
@require_http_methods(["GET", "POST"])
@csrf_exempt
def personas_list(request):
	if request.method == "GET":
		personas = Persona.objects.all().values('PersonaId', 'PersonaNombre', 'PersonaApellido', 'PersonaGenero', 'PersonaFechaN', 'PersonaJurado', 'Lugar_id', 'Usuario_id')
		return JsonResponse(list(personas), safe=False)
	elif request.method == "POST":
		try:
			data = json.loads(request.body)
			nombre = data.get('PersonaNombre')
			apellido = data.get('PersonaApellido')
			genero = data.get('PersonaGenero')
			fecha_n = data.get('PersonaFechaN')
			jurado = data.get('PersonaJurado')
			lugar_id = data.get('Lugar')
			usuario_id = data.get('Usuario')
			if not all([nombre, apellido, genero, fecha_n, jurado is not None, lugar_id, usuario_id]):
				return JsonResponse({'error': 'Todos los campos son requeridos'}, status=400)
			persona = Persona.objects.create(
				PersonaNombre=nombre,
				PersonaApellido=apellido,
				PersonaGenero=genero,
				PersonaFechaN=fecha_n,
				PersonaJurado=jurado,
				Lugar_id=lugar_id,
				Usuario_id=usuario_id
			)
			return JsonResponse({'PersonaId': persona.PersonaId, 'PersonaNombre': persona.PersonaNombre, 'PersonaApellido': persona.PersonaApellido, 'PersonaGenero': persona.PersonaGenero, 'PersonaFechaN': str(persona.PersonaFechaN), 'PersonaJurado': persona.PersonaJurado, 'Lugar': persona.Lugar_id, 'Usuario': persona.Usuario_id}, status=201)
		except Exception as e:
			return JsonResponse({'error': str(e)}, status=400)
	else:
		return HttpResponseNotAllowed(['GET', 'POST'])

@require_http_methods(["GET", "PUT", "DELETE"])
@csrf_exempt
def persona_detail(request, id):
	try:
		persona = Persona.objects.get(PersonaId=id)
	except Persona.DoesNotExist:
		return JsonResponse({'error': 'No existe la persona'}, status=404)

	if request.method == "GET":
		return JsonResponse({'PersonaId': persona.PersonaId, 'PersonaNombre': persona.PersonaNombre, 'PersonaApellido': persona.PersonaApellido, 'PersonaGenero': persona.PersonaGenero, 'PersonaFechaN': str(persona.PersonaFechaN), 'PersonaJurado': persona.PersonaJurado, 'Lugar': persona.Lugar_id, 'Usuario': persona.Usuario_id})
	elif request.method == "PUT":
		try:
			data = json.loads(request.body)
			nombre = data.get('PersonaNombre')
			apellido = data.get('PersonaApellido')
			genero = data.get('PersonaGenero')
			fecha_n = data.get('PersonaFechaN')
			jurado = data.get('PersonaJurado')
			lugar_id = data.get('Lugar')
			usuario_id = data.get('Usuario')
			if not all([nombre, apellido, genero, fecha_n, jurado is not None, lugar_id, usuario_id]):
				return JsonResponse({'error': 'Todos los campos son requeridos'}, status=400)
			persona.PersonaNombre = nombre
			persona.PersonaApellido = apellido
			persona.PersonaGenero = genero
			persona.PersonaFechaN = fecha_n
			persona.PersonaJurado = jurado
			persona.Lugar_id = lugar_id
			persona.Usuario_id = usuario_id
			persona.save()
			return JsonResponse({'PersonaId': persona.PersonaId, 'PersonaNombre': persona.PersonaNombre, 'PersonaApellido': persona.PersonaApellido, 'PersonaGenero': persona.PersonaGenero, 'PersonaFechaN': str(persona.PersonaFechaN), 'PersonaJurado': persona.PersonaJurado, 'Lugar': persona.Lugar_id, 'Usuario': persona.Usuario_id})
		except Exception as e:
			return JsonResponse({'error': str(e)}, status=400)
	elif request.method == "DELETE":
		persona.delete()
		return HttpResponse(status=204)
	else:
		return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])

# --- Registro ---
@require_http_methods(["GET", "POST"])
@csrf_exempt
def registros_list(request):
	if request.method == "GET":
		registros = Registro.objects.all().values('RegistrosId', 'DocId', 'Persona_id')
		return JsonResponse(list(registros), safe=False)
	elif request.method == "POST":
		try:
			data = json.loads(request.body)
			docid = data.get('DocId')
			persona_id = data.get('Persona')
			if docid is None or not persona_id:
				return JsonResponse({'error': 'DocId y Persona son requeridos'}, status=400)
			registro = Registro.objects.create(DocId=docid, Persona_id=persona_id)
			return JsonResponse({'RegistrosId': registro.RegistrosId, 'DocId': registro.DocId, 'Persona': registro.Persona_id}, status=201)
		except Exception as e:
			return JsonResponse({'error': str(e)}, status=400)
	else:
		return HttpResponseNotAllowed(['GET', 'POST'])

@require_http_methods(["GET", "PUT", "DELETE"])
@csrf_exempt
def registro_detail(request, id):
	try:
		registro = Registro.objects.get(RegistrosId=id)
	except Registro.DoesNotExist:
		return JsonResponse({'error': 'No existe el registro'}, status=404)

	if request.method == "GET":
		return JsonResponse({'RegistrosId': registro.RegistrosId, 'DocId': registro.DocId, 'Persona': registro.Persona_id})
	elif request.method == "PUT":
		try:
			data = json.loads(request.body)
			docid = data.get('DocId')
			persona_id = data.get('Persona')
			if docid is None or not persona_id:
				return JsonResponse({'error': 'DocId y Persona son requeridos'}, status=400)
			registro.DocId = docid
			registro.Persona_id = persona_id
			registro.save()
			return JsonResponse({'RegistrosId': registro.RegistrosId, 'DocId': registro.DocId, 'Persona': registro.Persona_id})
		except Exception as e:
			return JsonResponse({'error': str(e)}, status=400)
	elif request.method == "DELETE":
		registro.delete()
		return HttpResponse(status=204)
	else:
		return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])

@require_http_methods(["GET", "POST"])
@csrf_exempt
def departamentos_list(request):
	if request.method == "GET":
		departamentos = Departamento.objects.all().values('DepartamentoId', 'DepartamentoNombre')
		return JsonResponse(list(departamentos), safe=False)
	elif request.method == "POST":
		try:
			data = json.loads(request.body)
			nombre = data.get('DepartamentoNombre')
			if not nombre:
				return JsonResponse({'error': 'DepartamentoNombre es requerido'}, status=400)
			departamento = Departamento.objects.create(DepartamentoNombre=nombre)
			return JsonResponse({'DepartamentoId': departamento.DepartamentoId, 'DepartamentoNombre': departamento.DepartamentoNombre}, status=201)
		except Exception as e:
			return JsonResponse({'error': str(e)}, status=400)
	else:
		return HttpResponseNotAllowed(['GET', 'POST'])

@require_http_methods(["GET", "PUT", "DELETE"])
@csrf_exempt
def departamento_detail(request, id):
	try:
		departamento = Departamento.objects.get(DepartamentoId=id)
	except Departamento.DoesNotExist:
		return JsonResponse({'error': 'No existe el departamento'}, status=404)

	if request.method == "GET":
		return JsonResponse({'DepartamentoId': departamento.DepartamentoId, 'DepartamentoNombre': departamento.DepartamentoNombre})
	elif request.method == "PUT":
		try:
			data = json.loads(request.body)
			nombre = data.get('DepartamentoNombre')
			if not nombre:
				return JsonResponse({'error': 'DepartamentoNombre es requerido'}, status=400)
			departamento.DepartamentoNombre = nombre
			departamento.save()
			return JsonResponse({'DepartamentoId': departamento.DepartamentoId, 'DepartamentoNombre': departamento.DepartamentoNombre})
		except Exception as e:
			return JsonResponse({'error': str(e)}, status=400)
	elif request.method == "DELETE":
		departamento.delete()
		return HttpResponse(status=204)
	else:
		return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])
