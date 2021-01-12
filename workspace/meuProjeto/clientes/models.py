from django.db import models

# Create your models here.

# comandos
# python manage.py makemigrations
# python manage.py migrate
class Cliente(models.Model):
    name = models.CharField(max_length=70, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name