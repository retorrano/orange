from django.forms import ModelForm
from django import forms
from .models import Test

class TestAddForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

class TestEditForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'