from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'ism', 'familya', 'yosh', 'tugilgan_sana', 
            'manzil', 'telefon', 'email', 'tajriba', 'loyihalar', 'qoshimcha'
        ]
