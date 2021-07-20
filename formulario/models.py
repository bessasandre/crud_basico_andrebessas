from django.db import models


class Formulario(models.Model):
       nome = models.CharField(max_length=20)
       sobrenome = models.CharField(max_length=40)
       idade = models.IntegerField()
       nascimento = models.DateTimeField()
       email = models.EmailField()
       apelido = models.CharField(max_length=50)
       observacao = models.CharField(max_length=100)


