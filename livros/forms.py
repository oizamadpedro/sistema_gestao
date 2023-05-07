from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    finalizado = forms.BooleanField(widget=forms.CheckboxInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = Livro
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
