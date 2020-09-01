from django.urls import path
from .import views

app_name="usersapp"
urlpatterns = [
    path('login/',views.login, name='login'),
]