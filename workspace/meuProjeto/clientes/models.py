from django.db import models

# Create your models here.
# Documentação
# https://docs.djangoproject.com/en/3.1/ref/models/fields/#model-field-types


class Produto(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CPF(models.Model):
    numero = models.CharField(max_length=11)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.numero


# comandos
# python manage.py makemigrations
# python manage.py migrate
class Cliente(models.Model):
    name = models.CharField(max_length=70, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()
    # OneToOneField = Um para Um
    cpf = models.OneToOneField(CPF, blank=True, null=True, on_delete=models.CASCADE)
    # ManyToManyField = Muitos para Muitos
    produtos = models.ManyToManyField(Produto, blank=True, null=True)
    foto = models.ImageField(upload_to='cliente_fotos', height_field=None, width_field=None)

    def __str__(self):
        return self.name


class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao + ' - ' + self.numero