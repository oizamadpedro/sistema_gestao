from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, generics, filters
from livros.models import Livro
from livros.forms import LivroForm
from livros.serializer import LivroSerializer


class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    http_method_names = ['get', 'post', 'put', 'path']

def gestao(request):
    livros = Livro.objects.all().values()
    context = {"livros":livros}
    return render(request, 'galeria/gestao.html', context)

def create(request):
    form = LivroForm
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gestao')
    return render(request, 'galeria/create.html', {'form': form})

def editar(request, livro_id):
    
    livro = Livro.objects.get(pk=livro_id)
    form = LivroForm(instance=livro)


    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('/gestao')
        pass

    return render(request, 'galeria/editar.html', {'form': form, 'livro': livro, 'livro_id': livro_id})

def deletar(request, livro_id): 
    livro = Livro.objects.get(id=livro_id)
    livro.delete()
    return redirect('/gestao')

def details(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)

    context = {'livro': livro}
    return render(request, 'galeria/details.html', context)




