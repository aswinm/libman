from django import forms
import datetime
class LendingForm(forms.Form):
	subscriberid = forms.CharField(max_length = 20)
	bookid = forms.CharField(max_length = 20)

class TransactionStatement(forms.Form):
	stdate = forms.DateField()
	enddate = forms.DateField()
