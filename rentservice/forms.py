from django import forms

class ServiceForm(forms.Form):
    client_address = forms.CharField()