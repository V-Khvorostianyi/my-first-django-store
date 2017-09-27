from django import forms



class SetQtyProductForm(forms.Form):
	name = forms.IntegerField(required=True)



