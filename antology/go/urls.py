from django.urls import path
from go import views


urlpatterns = [
    path('', views.check),
    path('about/', views.about, name='about'),
    path('genes/<slug:ph_slug>/', views.gene, name='gene'),
    path('add/', views.add, name='add'),
    path('add_tests/', views.add_tests, name='add_tests'),
    path('geneinfo/', views.info_table, name='info_table'),
    path('jsgeneinfo/', views.js_info_table, name='js_info_table'),
    path('contacts/', views.contacts_show, name='contacts'),
]