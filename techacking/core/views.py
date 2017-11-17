from django.shortcuts import render


# Views - Basicamente é como uma função do Python

def index (request):
    contexto = {
        'cursos':[
            'Desenvolvimento',
            'Sistemas'
        ],
        'faculdade':' TECHACKING',
        'titulo':'TECHACKING'


    }
    return render(request,'index.html',contexto)

def cursospos (request):
    contexto = {
        'titulo':'TecPos'

    }
    return render(request, 'cursospos.html', contexto)

def cursoscertificacao (request):
    return render(request, 'cursoscertificacao.html')

def cursosgraduacao (request):
    return render(request, 'cursosgraduacao.html')

def graduacaosistemas (request):
    return render(request, 'graduacaosistemas.html')

def graduacaoredes (request):
    return render(request, 'graduacaoredes.html')

def graduacaogames (request):
    return render(request, 'graduacaogames.html')

def graduacaohacking (request):
    return render(request, 'graduacaohacking.html')

def contato (request):
    return render (request, 'contato.html')

def matriculese (request):
    return render ( request, 'matriculese.html')

def login (request):
    return render (request, 'login.html')

def loginaluno (request):
    return render (request, 'loginaluno.html')

def loginprofessor (request):
    return render (request, 'loginprofessor.html')

def logincoordenador (request):
    return render (request, 'logincoordenador.html')