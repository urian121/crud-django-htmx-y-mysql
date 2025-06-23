from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Aspirante
from django.contrib import messages
from django.template.loader import render_to_string

def inicio(request):
    return listar_aspirantes(request)


def modal_add_aspirante(request):
    return render(request, 'aspirantes/modales/modalAdd.html')

def add_aspirante(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            curso = request.POST.get('curso')
            sexo = request.POST.get('sexo')
            habla_ingles = request.POST.get('habla_ingles')
            
            if not nombre or not email or not curso or not sexo:
                return JsonResponse({'error': 'Todos los campos son obligatorios'}, status=400)
            
            aspirante = Aspirante(
                nombre=nombre,
                email=email,
                curso=curso,
                sexo=sexo,
                habla_ingles=habla_ingles == 'on'  # Convierte el checkbox a booleano
            )
            aspirante.save()

            messages.success(request, 'Aspirante registrado correctamente')
            html = render_to_string('aspirantes/fila.html', {'aspirante': aspirante}, request=request)
            return HttpResponse(html, status=201)
            
        except Exception as e:
            messages.error(request, 'Error al registrar aspirante: ' + str(e))
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)


def listar_aspirantes(request):
    aspirantes = Aspirante.objects.all()
    data = {
        'aspirantes': aspirantes
    }
    return render(request, 'aspirantes/index.html', data)




def cambiar_estado(request, id_aspirante):
    pass

def ver_aspirante(request, id_aspirante):
    pass

def editar_aspirante(request, id_aspirante):
    pass
    
def eliminar_aspirante(request, id_aspirante):
    pass