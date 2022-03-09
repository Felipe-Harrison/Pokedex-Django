
from multiprocessing import context
import re
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.core.files.storage import FileSystemStorage

from django.views.generic import DetailView, ListView, CreateView

# para redirecionar o usuario
from django.urls import reverse_lazy

from .models import pokemon

class PokemonListView(ListView):
    model = pokemon

class PokemonDetailView(DetailView):

    model = pokemon

def Create_Pokemon(request):

    # para somente executar quando for POST
    if(request.method == "POST"):

        new_number = request.POST.get('pokemon-number')
        new_image = request.FILES['pokemon-url']
        # com arquivo pega Files não get
        #new_image = request.POST.get('pokemon-url')
        new_image_name = str(new_image)

        new_tipo = request.POST.getlist('pokemon-type')
        if(len(new_tipo) <= 1):
            new_tipo.append('null')
        
        new_nome = request.POST.get('pokemon-name')
        # Personalizar o card do pokemon pelo nome
        if str(new_nome).find("_42") != -1:
            new_raridade = "lendario"
            new_nome = str(new_nome)[0:-3]
        elif str(new_nome).find("_old") != -1:
            new_raridade = "old"
            new_nome = str(new_nome)[0:-4]
        else:
            new_raridade = "comun"
        
        pokemon.objects.create(number = new_number,name= new_nome,image=new_image,image_name = new_image_name,type1 = new_tipo[0],type2 = new_tipo[1],raridade = new_raridade)
        print("Pokemon Criado")
        
        # para retornar para alguma pagina
        return HttpResponseRedirect("/listar")

    context = {}
    # renderizar a pagina html
    return render(request,"cadastro_poke/cadastro.html",context)


def Edit_Pokemon(request,pk):
    print(request.method)
 
    # Deletar metodo
    if(request.method == "POST" and "delete-poke" in request.POST):
        poke = pokemon.objects.get(id=pk)
        poke.delete()
        print("Pokemon Deletado")
        return HttpResponseRedirect("/listar")
    
    # Editar
    if(request.method == "POST"):
        poke = pokemon.objects.filter(id=pk)

        new_nome = request.POST.get('pokemon-name')
         # Personalizar o card do pokemon pelo nome
        if str(new_nome).find("_42") != -1:
            new_raridade = "lendario"
            new_nome = str(new_nome)[0:-3]
        elif str(new_nome).find("_00") != -1:
            new_raridade = "comun"
            new_nome = str(new_nome)[0:-3]
        elif str(new_nome).find("_old") != -1:
            new_raridade = "old"
            new_nome = str(new_nome)[0:-4]
        else:
            new_raridade = pokemon.objects.get(id=pk).raridade
        
        new_number = request.POST.get('pokemon-number')

        new_tipo = request.POST.getlist('pokemon-type')
        if(len(new_tipo) <= 1):
            new_tipo.append('null')

        imagemInput = request.POST.get('pokemon-url')
        if imagemInput != "":
            new_image = request.FILES['pokemon-url']
            new_image_name = str(new_image)
        else:
            new_image = pokemon.objects.get(id=pk).image
            new_image_name = pokemon.objects.get(id=pk).image_name

        poke.update(number = new_number,name= new_nome,image=new_image,image_name = new_image_name,type1 = new_tipo[0],type2 = new_tipo[1],raridade = new_raridade)
        print("Pokemon Editado")
        # para retornar para alguma pagina
        return HttpResponseRedirect("/listar")

    poke = pokemon.objects.get(id=pk)
    context = {"nome":poke.name,"num":poke.number,"image_name":poke.image_name,"tipo1":poke.type1,"tipo2":poke.type2}
    return render(request,"pokemon_edit/edicao.html",context)

