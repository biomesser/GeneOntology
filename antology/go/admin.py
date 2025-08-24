from django.contrib import admin

# Register your models here.
from .models import Phenotype, Genes

admin.site.register(Genes)
admin.site.register(Phenotype)