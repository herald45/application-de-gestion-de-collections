from django import forms
from .models import Collec

class CollecForm(forms.ModelForm):
    class Meta:
        model = Collec
        fields = ['title', 'description']
        labels = {
            "title" : "Titre",
            "description" : "Description"
        }
