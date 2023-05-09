from django.shortcuts import render

# Create your views here.
def index(request):
    meu_nome = 'Washington Junior'
    listas_frutas = ['Laranja', 'Maca', 'Banana']
    context = {
        'nome': meu_nome,
        'frutas': listas_frutas
    }
    return render(request, 'index.html', context)