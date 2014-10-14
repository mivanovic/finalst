__author__ = 'Final'

from django import forms


class EmailForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=30)
    message = forms.CharField(max_length=30, required=True)