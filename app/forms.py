
from django import forms
from app.models import *

class TopicForm(forms.Form):
    tn=forms.CharField()

class WebpageForm(forms.Form):
    tn=forms.ModelChoiceField(queryset=Topic.objects.all())
    n=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()

class AccessRecordForm(forms.Form):
    n=forms.ModelChoiceField(queryset=Webpage.objects.all())
    d=forms.DateField()
    a=forms.CharField()