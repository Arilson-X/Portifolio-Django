from django.shortcuts import render, get_object_or_404, redirect

from portfolio.models import Projeto,Experiencia,Curso

def index(request):
    projetos = Projeto.objects.order_by("-data")
    experiencias = Experiencia.objects.order_by("-data_inicio")
    cursos = Curso.objects.order_by("-data",)

    projetos = projetos[:5]
    experiencias = experiencias[:5]
    cursos = cursos[:5]
    return render(request, 'portfolio/index.html',{
        "projetos":projetos,
        "experiencias":experiencias,
        "cursos":cursos
    })

def projetos(request):
    projetos = Projeto.objects.order_by("-data")
    return render(request, 'portfolio/projetos.html',{
        "projetos":projetos,
    })

def projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto,pk=projeto_id)
    return render(request, 'portfolio/projeto.html', {"projeto": projeto})

def experiencias(request):
    experiencias = Experiencia.objects.order_by("-data_inicio")
    return render(request, 'portfolio/experiencias.html',{
        "experiencias":experiencias,
    })

def cursos(request):
    cursos = Curso.objects.order_by("-data")
    return render(request, 'portfolio/cursos.html',{
        "cursos":cursos,
    })

def curso(request, curso_id):
    curso = get_object_or_404(Curso,pk=curso_id)
    return render(request, 'portfolio/curso.html', {"curso": curso})

def contato(request):
    return render(request, template_name='portfolio/contato.html')


def filtro(request, tipo):
    cursos = Curso.objects.order_by('-data').filter(tipo=tipo)
    projetos = Projeto.objects.order_by('-data').filter(tipo=tipo)
    return render(request, 'portfolio/index.html',{
        "projetos":projetos,
        "cursos":cursos
    })
