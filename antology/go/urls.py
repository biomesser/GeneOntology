from django.urls import path
from go import views

urlpatterns = [
    path('', views.go_show, name='go'),
]