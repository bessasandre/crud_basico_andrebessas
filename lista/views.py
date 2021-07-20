from django.shortcuts import render
from django.http import HttpResponse

from formulario import forms
from formulario import models

def cadastro(request):
   form = forms.FormularioForm()
   if request.method == "POST":
     print('vou salvar os dados')
     form = forms.FormularioForm(request.POST)
     print(form)
     if form.is_valid():
        form.save()
     else:
        print('ERRO')
   formularios_list = models.Formulario.objects.order_by('nome');
   data_dict = {'form':form , "formularios_records" : formularios_list}

   return render(request, 'formulario/formulario.html', data_dict)