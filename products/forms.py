from django import forms
from .models import *

class SetQtyProductForm(forms.Form):
    qty = forms.IntegerField(default=1)



