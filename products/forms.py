from django import forms
from orders.models import *


class SetQtyProductForm(forms.ModelForm):
	class Meta:
		model = Order
		exclude = [""]


