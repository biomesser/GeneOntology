import django_tables2 as tables

from .models import Genes

class GenesTable(tables.Table):
    class Meta:
        model = Genes
        template_name = "django_tables2/bootstrap5.html"
        fields = ('gene', 'link_to_pheno', 'gene_source',)