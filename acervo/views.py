from django.shortcuts import render
from .models import Livro, Tipo

def lista_livros(request):
    livros = Livro.objects.all()
    nome = request.GET.get('nome')
    tipo = request.GET.get('tipo')
    categoria = request.GET.get('categoria')
    if nome: livros = livros.filter(titulo__icontains=nome)
    if tipo: livros = livros.filter(tipo_acervo=nome)
    if categoria: livros = livros.filter(categoria=categoria)
    return render(
        request, 'lista.html',
        {'livros': livros} # envia ao template
    )
    
def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save() # grava no banco
            return redirect('lista')
    else:
        form = LivroForm()
    return render(request, 'acervo/form.html', {'form': form})   