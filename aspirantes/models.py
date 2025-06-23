from django.db import models

class Aspirante(models.Model):
    CURSOS = [
        ('HTMX', 'HTMX'),
        ('PHP', 'PHP'),
        ('JS', 'JS'),
        ('HTML', 'HTML'),
        ('REACT', 'React'),
    ]

    SEXOS = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=10, choices=CURSOS)
    sexo = models.CharField(max_length=10, choices=SEXOS)
    habla_ingles = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tbl_aspirantes'
        ordering = ['-created_at']
