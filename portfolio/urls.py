from django.urls import path
from portfolio.views import index, projetos, cursos, experiencias, contato, projeto, curso, filtro


urlpatterns = [
    path('', index, name='index'),
    path('projetos',projetos,name='projetos'),
    path('projeto/<int:projeto_id>',projeto,name='projeto'),
    path('cursos',cursos,name='cursos'),
    path('curso/<int:curso_id>',curso,name='curso'),
    path('experiencias',experiencias,name='experiencias'),
    path('contato',contato,name='contato'),
    path('filtro/<str:tipo>',filtro,name='filtro')
]