from django.contrib import admin
from django.urls import path, include
from livros.models import Livro
from livros.views import LivrosViewSet
from livros.views import gestao, deletar, create, editar, details
from rest_framework import routers, permissions
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('livros', LivrosViewSet, basename='Livros')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('gestao/', gestao, name='gestao'),
    path('create/', create, name='create'),
    path('gestao/editar/<int:livro_id>', editar, name='editar'),
    path('deletar/<int:livro_id>', deletar, name='deletar'),
    path('gestao/details/<int:livro_id>', details, name='details'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
