from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, Http404
from django.views.decorators.http import require_http_methods
import json
from .models import Departamento

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
