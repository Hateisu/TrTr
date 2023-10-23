from django.urls import path

#Импортируем все подключения из views 
from . import views

#Прописываем возможные url для этого приложения
urlpatterns = [

    #Главная Страница
    path('', views.main_page, name='home'),

    #Страница Подбора
    path('tours/', views.tours, name='tours'),

    #Страница для попытки подбора через Ajax
    path('tours_filter/', views.tours_filter, name='tours_filter'),

    #Странца Google-form
    path('forms/', views.forms, name='forms'),
]