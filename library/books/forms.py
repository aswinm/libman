from django import forms

class BookAddForm(forms.Form):
	bid  = forms.CharField(max_length = 10, required = False)
	bname = forms.CharField(max_length = 100, required = False)
	author = forms.CharField(max_length = 30, required = False)
	TotBooks =  forms.IntegerField(required = False)
	AvlBooks =  forms.IntegerField(required = False)
