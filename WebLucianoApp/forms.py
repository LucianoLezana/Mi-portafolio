from django import forms
from .models import ContactMe


class FormContactMe(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ('name', 'subject', 'email', 'menssage')
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'menssage':forms.Textarea(attrs={'class':'form-control'}),
            
                
        }