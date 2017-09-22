from django import forms
from .models import *

class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phones = forms.CharField(required=True)


