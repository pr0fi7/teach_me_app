# cards/forms.py

from django import forms
from .models import Card


class DocumentUploadForm(forms.Form):
    document = forms.FileField()
    box = forms.IntegerField(min_value=0)
    question_number = forms.IntegerField(min_value=1, max_value=100, help_text='Enter the number of questions to generate for each chunk of text')

class CardCreateForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["question", "answer", "box"]

