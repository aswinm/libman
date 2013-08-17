from django import forms

class SubscriberForm(forms.Form):
	CHOICE = [('M','Male'),('F','Female')]
	sid = forms.CharField(max_length = 20 , required =False)
	name = forms.CharField(max_length = 100, required = False)
	gender = forms.ChoiceField(choices = CHOICE, widget = forms.RadioSelect(), required = False)
	contact  = forms.CharField(max_length = 11, required = False)
	mail = forms.EmailField(max_length = 30, required = False)

	


