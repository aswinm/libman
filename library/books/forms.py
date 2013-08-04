from django import forms

class BookAddForm(forms.Form):
	bid  = forms.CharField(max_length = 10)
	bname = forms.CharField(max_length = 100)
	author = forms.CharField(max_length = 30)
	TotBooks =  forms.IntegerField()
	AvlBooks =  forms.IntegerField()
