from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Aspirante
from django.contrib import messages
from django.template.loader import render_to_string

# Función para generar un nombre único para los archivos
import os
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile


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
            imagen_perfil = request.FILES.get('imagen_perfil')
            archivo_pdf = request.FILES.get('archivo_pdf')
            
            # Renombrar archivos
            if imagen_perfil and archivo_pdf:
                imagen_perfil = generate_unique_filename(imagen_perfil)
                archivo_pdf = generate_unique_filename(archivo_pdf)
            
            aspirante = Aspirante(
                nombre=nombre,
                email=email,
                curso=curso,
                sexo=sexo,
                habla_ingles=habla_ingles == 'on',  # Convierte el checkbox a booleano
                imagen_perfil=imagen_perfil,
                archivo_pdf=archivo_pdf
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
    return render(request, 'aspirantes/index.html', {'aspirantes': aspirantes})


def cambiar_estado(request, id_aspirante):
    try:
        aspirante = Aspirante.objects.get(id=id_aspirante)
        aspirante.aceptado = not aspirante.aceptado
        aspirante.save()
        
        # Renderizar la fila completa actualizada
        messages.success(request, 'Estado actualizado correctamente')
        html = render_to_string('aspirantes/fila.html', {'aspirante': aspirante}, request=request)
        return HttpResponse(html, status=200)
        
    except Aspirante.DoesNotExist:
        messages.error(request, 'Aspirante no encontrado')
        return HttpResponse(status=404)
    except Exception as e:
        messages.error(request, 'Error al cambiar estado: ' + str(e))
        return HttpResponse(status=500)

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
            
            # Actualizar campos básicos
            aspirante.nombre = request.POST.get('nombre')
            aspirante.email = request.POST.get('email')
            aspirante.curso = request.POST.get('curso')
            aspirante.sexo = request.POST.get('sexo')
            aspirante.habla_ingles = request.POST.get('habla_ingles') == 'on'
            
            # Manejar imagen de perfil
            nueva_imagen = request.FILES.get('imagen_perfil')
            if nueva_imagen:
                nueva_imagen = generate_unique_filename(nueva_imagen)
                aspirante.imagen_perfil = nueva_imagen # Actualizar imagen
            
            # Manejar archivo PDF
            nuevo_pdf = request.FILES.get('archivo_pdf')
            if nuevo_pdf:
                nuevo_pdf = generate_unique_filename(nuevo_pdf)
                aspirante.archivo_pdf = nuevo_pdf  # Actualizar PDF
            
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


# Función auxiliar para renombrar archivos
def generate_unique_filename(file):
    extension = os.path.splitext(file.name)[1]
    unique_name = f'{uuid.uuid4()}{extension}'
    return SimpleUploadedFile(unique_name, file.read())