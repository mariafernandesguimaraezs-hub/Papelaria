from django.urls import path
from .views import listar_categorias
from .views import listar_produtos

urlpatterns =[
    path('categorias', listar_categorias),
    path('produtos', listar_produtos)
]