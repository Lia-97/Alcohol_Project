from django.urls import path
from mainapp import views

urlpatterns = [
    path('index/',views.index, name='index'),
]