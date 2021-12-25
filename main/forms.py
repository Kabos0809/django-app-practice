from django import forms
from .models import article_form

class articleform(forms.ModelForm):
    class Meta():
        model = article_form
        fields = ('title', 'comments')