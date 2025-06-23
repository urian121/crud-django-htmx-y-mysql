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

# Función para obtener y preparar los datos de un aspirante
def ver_aspirante(request, id_aspirante):
    data = _get_aspirante_data(request, id_aspirante)
    if data:
        return render(request, 'aspirantes/modales/modalView.html', data)
    return HttpResponse(status=404)

# Función para obtener y preparar los datos de un aspirante
def modal_update_aspirante(request, id_aspirante):
    data = _get_aspirante_data(request, id_aspirante)
    if data:
        return render(request, 'aspirantes/modales/modalUpdate.html', data)
    return HttpResponse(status=404)

def editar_aspirante(request, id_aspirante):
    if request.method == 'POST':
        try:
            aspirante = Aspirante.objects.get(id=id_aspirante)
            aspirante.nombre = request.POST.get('nombre')
            aspirante.email = request.POST.get('email')
            aspirante.curso = request.POST.get('curso')
            aspirante.sexo = request.POST.get('sexo')
            aspirante.habla_ingles = request.POST.get('habla_ingles') == 'on'
            aspirante.save()
            messages.success(request, 'Aspirante actualizado correctamente')
            html = render_to_string('aspirantes/fila.html', {'aspirante': aspirante}, request=request)
            return HttpResponse(html, status=200)
        except Exception as e:
            messages.error(request, 'Error al actualizar aspirante: ' + str(e))
            return JsonResponse({'error': str(e)}, status=500)
    
    return HttpResponse(status=204)  # Respuesta vacía, ideal para HTMX
    
    
def modal_delete_aspirante(request, id_aspirante):
    data = _get_aspirante_data(request, id_aspirante)
    if data:
        return render(request, 'aspirantes/modales/modalDelete.html', data)
    return HttpResponse(status=404)


def eliminar_aspirante(request, id_aspirante):
    try:
        aspirante = Aspirante.objects.get(id=id_aspirante)
        aspirante.delete()
        messages.success(request, 'Aspirante eliminado correctamente')
        return HttpResponse(status=204) # Respuesta vacía, ideal para HTMX
    except Aspirante.DoesNotExist:
        messages.error(request, 'Aspirante no encontrado')
        return HttpResponse(status=404) # Respuesta vacía, ideal para HTMX
    except Exception as e:
        messages.error(request, f'Error al eliminar aspirante: {str(e)}')
        return HttpResponse(status=500) # Respuesta vacía, ideal para HTMX


# Función auxiliar para obtener y preparar los datos de un aspirante
def _get_aspirante_data(request, id_aspirante):
    try:
        aspirante = Aspirante.objects.get(id=id_aspirante)
        return {'aspirante': aspirante}
    except Aspirante.DoesNotExist:
        messages.error(request, 'Aspirante no encontrado')
        return None