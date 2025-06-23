# CRUD Django con HTMX y MySQL

Un proyecto de ejemplo que implementa un CRUD completo usando Django como backend, HTMX para interacciones sin recarga de página y MySQL como base de datos.

![image](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/refs/heads/master/crud-django-htmx-mysql.gif)

## Características Principales

- Interfaz moderna con Bootstrap 5
- Operaciones CRUD completas (Crear, Leer, Actualizar, Eliminar)
- Uso de HTMX para interacciones sin recarga de página
- Manejo de archivos (imágenes y PDFs)
- Visualización previa de PDFs
- Estado de aceptación/rechazo de aspirantes
- Tabla con paginación y ordenamiento


## Instalación

1. Crear y activar entorno virtual:
```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar la base de datos MySQL:
- Crear una base de datos MySQL
- Actualizar las credenciales en `project_core/settings.py`

5. Aplicar las migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Crear un superusuario (opcional):
```bash
python manage.py createsuperuser
```

7. Ejecutar el servidor:
```bash
python manage.py runserver
```

## Tecnologías Utilizadas

- Backend: Django
- Frontend: Bootstrap 5, HTMX
- Base de datos: MySQL
- JavaScript: HTMX, DataTables
- UI Components: Bootstrap Icons

## Funcionalidades Principales

1. **Listado de Aspirantes**
   - Tabla con paginación y ordenamiento
   - Estado visual de aceptación/rechazo
   - Búsqueda y filtrado

2. **Crear Aspirante**
   - Formulario modal para agregar nuevo aspirante
   - Subida de imagen de perfil
   - Subida de archivo PDF (CV)
   - Validación de campos

3. **Ver Detalles**
   - Modal para ver información completa
   - Vista previa de imagen de perfil
   - Vista previa de PDF

4. **Actualizar Aspirante**
   - Modal para editar información
   - Actualización de imagen y PDF
   - Mantenimiento de archivos existentes

5. **Eliminar Aspirante**
   - Confirmación de eliminación
   - Eliminación segura


## 🙌 Cómo puedes apoyar 📢:

✨ **Comparte este proyecto** con otros desarrolladores para que puedan beneficiarse 📢.

☕ **Invítame un café o una cerveza 🍺**:
   - [Paypal](https://www.paypal.me/iamdeveloper86) (`iamdeveloper86@gmail.com`).

### ⚡ ¡No olvides SUSCRIBIRTE a la [Comunidad WebDeveloper](https://www.youtube.com/WebDeveloperUrianViera?sub_confirmation=1)!


#### ⭐ **Déjanos una estrella en GitHub**:
   - Dicen que trae buena suerte 🍀.
**Gracias por tu apoyo 🤓.**