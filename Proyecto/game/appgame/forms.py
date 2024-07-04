from django import forms

class ConsolaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50)
    empresa = forms.CharField(max_length=50)
    precio = forms.IntegerField()

class AccesorioForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50)
    empresa = forms.CharField(max_length=50)
    precio = forms.IntegerField()

class JuegoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    categoria = forms.CharField(max_length=50)
    empresa = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    
    
