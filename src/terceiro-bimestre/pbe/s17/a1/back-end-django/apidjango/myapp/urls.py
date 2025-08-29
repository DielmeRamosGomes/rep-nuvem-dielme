from django.urls import path, include
from .views import SalvarLivroAPIView
from django.contrib import admin

urlpatterns = [
    path('livros/', SalvarLivroAPIView.as_view(), name='salvar-livro'),
    path('admin/', admin.site.urls),
    path('api/', include('meu_app.urls')),
]

