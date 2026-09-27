from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('index/<str:user>', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register")
]