from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about_url'),
    path('add/', views.add, name='add_url'),
    path('some/', views.some),
    path('thisis/', views.user),
    path('set/', views.set),

]
