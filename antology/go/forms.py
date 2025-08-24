from django import forms
from .models import Phenotype, Genes, Rs, Transcripts

class AddBioInfo(forms.Form):
    gene = forms.CharField(max_length=15, label='Gene_symbol')
    transcript = forms.CharField(max_length=30, label='Transcript')
