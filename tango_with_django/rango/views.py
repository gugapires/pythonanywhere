from django.shortcuts import render
from rango.models import Category


def index(request):
    #context_dict = {'boldmessage': "Olá BSI6, este texto veio da view!"}#comentar aqui pois vou usar as informações da model, model dinamica
    category_list = Category.objects.order_by('name')[:5] # aqui era pra usar likes mas ta dando pauu
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context=context_dict)


#estou na pagina 68

def about(request):
    context_dict = {'bunda': 'Gustavo Miranda'}
    # a variavel bunda pega o valor que esta depois dos
    # dois pontos logo la no html eu coloco {{ bunda }}
    # que vai mostrar o resultado que tem nela

    return render(request, 'rango/about.html', context=context_dict)

def teste(request):
    variavel = 1+1
    context_dict = {'oi': variavel}

    return render(request, 'rango/teste.html', context=context_dict)

