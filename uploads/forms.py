from django import forms 
from .models import document
class DocumentForm(forms.ModelForm):    
    class Meta:        
        model = document     
        fields = ['title', 'file']   # or ['title', 'image']