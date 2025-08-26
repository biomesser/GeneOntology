from django import forms
from .models import Phenotype, Genes, Rs, Transcripts

class AddBioInfo(forms.Form):
    gene = forms.CharField(max_length=15, label='Gene_symbol')
    transcript = forms.CharField(max_length=30, label='Transcript')


class AddGeneForm(forms.ModelForm):
#    link_to_pheno = forms.ModelChoiceField(queryset=Phenotype.objects.all(), empty_label="No_affected_phenotype", label="Phenotype")
#    transcript = forms.ModelChoiceField(queryset=Transcripts.objects.all(), required=False, empty_label="No_transcript_data", label="Transcript")
    class Meta:
        model = Genes
        fields = ['gene', 'link_to_pheno',]
        widgets = {
            'gene': forms.TextInput(attrs={'class': 'form-input'}),
        }
