from django.db import models

class Aspirante(models.Model):
    CURSOS = [
        ('Full Stack', 'Full Stack'),
        ('Data Science', 'Data Science'),
        ('Machine Learning', 'Machine Learning'),
        ('DevOps', 'DevOps'),
    ]

    SEXOS = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=20, choices=CURSOS)
    sexo = models.CharField(max_length=10, choices=SEXOS)
    habla_ingles = models.BooleanField(default=False)
    imagen_perfil = models.ImageField(upload_to='aspirantes/imagenes/', null=True, blank=True)
    archivo_pdf = models.FileField(upload_to='aspirantes/pdf/', null=True, blank=True)
    aceptado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tbl_aspirantes'
        ordering = ['-created_at']
