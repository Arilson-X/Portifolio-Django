from django.contrib import admin

from portfolio.models import Curso, Experiencia, Projeto

class ListandoCursos(admin.ModelAdmin):
    list_display = ('id','nome','plataforma','tipo','data',)
    list_display_links = ('id','nome',)
    search_fields = ('nome',)
    list_filter = ('tipo',)
    list_per_page = 10

class ListandoExperiencias(admin.ModelAdmin):
    list_display = ('id','empresa',)
    list_display_links = ('id','empresa',)
    search_fields = ('empresa',)
    list_per_page = 5

class ListandoProjetos(admin.ModelAdmin):
    list_display = ('id','nome','tipo','data',)
    list_display_links = ('id','nome',)
    search_fields = ('nome',)
    list_filter = ('tipo',)
    list_per_page = 10

admin.site.register(Curso, ListandoCursos)
admin.site.register(Experiencia, ListandoExperiencias)
admin.site.register(Projeto, ListandoProjetos)