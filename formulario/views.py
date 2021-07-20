from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from . import forms
from . import models
# Create your views here.

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



def delete(request,id):
    try:
       models.Formulario.objects.filter(id=id).delete()
       form = forms.FormularioForm();
       formularios_list = models.Formulario.objects.order_by('nome')
       data_dict = {'form':form , "formularios_records" : formularios_list}
       return render(request,'formulario/formulario.html', data_dict)
    except:
       return HttpResponseNotAllowed()

def update(request, id):
    item = models.Formulario.objects.get(id=id);
    if request.method == "GET":
        form = forms.FormularioForm(initial={'nome': item.nome})

        data_dict = {'form': form}
        return render(request, 'formulario/formulario_update.html', data_dict)
    else:
        form = forms.FormularioForm(request.POST)
        item.nome = form.data['nome']
        item.save()
        formularios_list = models.Formulario.objects.order_by('nome')
        data_dict = {'form':form , "formularios_records" : formularios_list}
        return render(request, 'formulario/formulario.html', data_dict)


