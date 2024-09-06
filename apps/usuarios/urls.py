from django.urls import path

from apps.usuarios.views import login, cadastro, logout

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
]

# todos fazem link com as urls apresentadas no site, logo serão chamadas de acordo com a url apresentada no site.