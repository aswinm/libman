from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader
from models import Subscriber
from login import views
from forms import SubscriberForm

def index(request):
	if not views.if_authenticated():
		page = loader.get_template('login.html')
		cont = RequestContext(request)
		return HttpResponse(page.render(cont))

	t = loader.get_template('subscribers_index.html')
	c = RequestContext(request)
	return HttpResponse(t.render(c))

def addSub(request):
	if not views.if_authenticated():
		t = loader.get_template('login.html')
		c = RequestContext(request)
		return HttpResponse(t.render(c))
	form = SubscriberForm(request.POST)
	if request.method == "POST":
		print "Method POST"
		if form.is_valid():
			print "VALID FORM"
			sub_details = Subscriber.objects.create(
					sid = form.cleaned_data['sid'],
					name = form.cleaned_data['name'],
					gender = form.cleaned_data['gender'],
					contact = form.cleaned_data['contact'],
					mail = form.cleaned_data['mail'],
					NoOfBooks = 0
					)
			sub_details.save()
			text = 'Subscriber added Successfully'
			t = loader.get_template('success.html')
			c = RequestContext(request, { 'text' : text })
			return HttpResponse(t.render(c))
		else:
			t = loader.get_template('add.html')
			text = 'Add Subscriber'
			c = RequestContext(request , { 'form' : form , 'text' : text})
			return HttpResponse(t.render(c))

	else:
		t = loader.get_template('add.html')
		text = 'Add Subscriber'
		c = RequestContext(request , { 'form' : form , 'text' : text})
		return HttpResponse(t.render(c))

# Create your views here.
