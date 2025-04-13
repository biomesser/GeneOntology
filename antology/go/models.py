from django.db import models

# Create your models here.
class Phenotype(models.Model):
    pheno = models.CharField(max_length=30)
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    slug=models.SlugField(max_length=30, db_index=True, verbose_name='URL_pheno', unique=True)

    def __str__(self):
        return self.pheno

class Genes(models.Model):
    gene=models.CharField(max_length=30)
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=30, db_index=True, verbose_name='URL_gene', unique=True)
    link_to_pheno = models.ManyToManyField(Phenotype, blank=True, related_name='link_pheno')
    gene_source = models.OneToOneField('Transcripts', on_delete=models.PROTECT, null=True, blank=True, related_name='tr_of_gene')


    def __str__(self):
        return self.gene
class Rs(models.Model):
    rs_name=models.CharField(max_length=30)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=30, db_index=True, verbose_name='URL_rs', unique=True)
    link_to_gene = models.ForeignKey(Genes, on_delete=models.PROTECT, null=True, related_name='rsset')


    def __str__(self):
        return self.rs_name

class Consorcium(models.Model):
    cons_name=models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=30, db_index=True, verbose_name='URL_cons', unique=True)

    def __str__(self):
        return self.cons_name

class Transcripts(models.Model):
    tr_name = models.CharField(max_length=40)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=30, db_index=True, verbose_name='URL_tr', unique=True)
