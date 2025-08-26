from django.urls import path
from go import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('add/', views.add_gene, name='add'),
    path('geneinfo/', views.info_table, name='info_table'),
    path('jsgeneinfo/', views.js_info_table, name='js_info_table'),
    path('contacts/', views.contacts_show, name='contacts'),
]