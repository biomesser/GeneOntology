from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify

from .forms import AddBioInfo, AddGeneForm
from .models import Phenotype, Genes


from django_tables2 import SingleTableView
from .tables import GenesTable

# Create your views here.


def contacts_show(request):
    return render(request, "go/contacts.html", {"title": "Contacts"})

def info_table(request):
    model = Genes.objects.all().prefetch_related("link_to_pheno")
    table = GenesTable(model)
    return render(request, "go/info_table.html", {"model": model, "table": table})


def js_info_table(request):
    db_data = Genes.objects.all()
    return render(request, "go/js_info_table.html", {"title": "JS_table", "db_data": db_data})


def about(request):
    return render(request, 'go/about.html', {'title': 'GO_antology', 'about': 'Что такое сайт GeneOntology'})

def go_show(request):
    return HttpResponse('z')

def base_page(request):
    menu = Phenotype.objects.all()
    url_list = []
    for x in menu:
        url_list.append('<a href="' + reverse('gene', args=(x.slug, )) + '">' + x.pheno + "</a>")
    print(url_list)
    #return HttpResponse(url_list)
    #return render(request, 'base.html', {'url_list': url_list})
    return render(request, 'base.html', {'title': 'Genetics_antology', 'menu': menu, 'url_list': url_list})
def gene(request, ph_slug):
    p = Phenotype.objects.get(slug = ph_slug)
    pheno_slug = ph_slug
    genes = p.link_pheno.all()
    cont = dict()
    for x in genes:
        all_rs_one_gene=x.rsset.all()
        l=[]
        transcript = x.gene_source
        print(dir(transcript))
        print('#################')
        l.append({x.gene + '_transcript is ': str(transcript)})
        for rs in all_rs_one_gene:
            l.append(rs.rs_name)
        cont[x.gene] = l

    return render(request, 'go/genes.html', {'title': 'genes', 'pheno_slug': pheno_slug, 'contented': 'GENES!', 'genes': cont})



def add(request):
    if request.POST:
        all_pheno=Phenotype.objects.all()
        for p in all_pheno:
            if p.pheno == request.POST['pheno']:
                g = Genes.objects.create(gene=request.POST['gene'], slug=slugify(request.POST['gene']))
                #Genes.link_pheno=Genes.objects.get(gene=request.POST['gene'])
                g.link_to_pheno.add(p)   #Phenotype.objects.get(pheno=request.POST['pheno']))
    return render(request, 'go/add.html')


def add_tests(request):
    if request.POST:
        form = AddBioInfo(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddBioInfo()
    return render(request, 'go/add_tests.html', {'form': form})


def add_gene(request):
    if request.method == "POST":
        form = AddGeneForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("js_info_table")
    else:
        form = AddGeneForm()

    data = {'title': 'add_gene', 'form': form}
    return render(request, 'go/add.html', data)


