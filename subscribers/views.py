from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader
from models import Subscriber
from login import views
from forms import SubscriberForm

flag = 0
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
	if request.method == "POST" and form.is_valid():
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

def search(request):
	if not views.if_authenticated():
		t = loader.get_template('login.html')
		c = RequestContext(request)
		return HttpResponse(t.render(c))
	t = loader.get_template('search_sub.html')
	c = RequestContext(request)
	return HttpResponse(t.render(c))

def searchdelete(request):
	if not views.if_authenticated():
		t = loader.get_template('login.html')
		c = RequestContext(request)
		return HttpResponse(t.render(c))
	global flag
	flag = 1
	t = loader.get_template('search_sub.html')
	c = RequestContext(request)
	return HttpResponse(t.render(c))

def display(request):
	if not views.if_authenticated():
		t = loader.get_template('login.html')
		c = RequestContext(request)
		return HttpResponse(t.render(c))
	global flag
	search_details = request.POST
	result = Subscriber.objects.filter(name__contains = search_details['name'])
	if not result:
		return HttpResponse('Subscriber not Found')
	t = loader.get_template('subscriber_display_delete.html')
	context = RequestContext(request , { 'sublist' : result, 'j' : flag })
	return HttpResponse(t.render(context))

def delete(request):
	if not views.if_authenticated():
		t = loader.get_template('login.html')
		c = RequestContext(request)
		return HttpResponse(t.render(c))
	delete_details = request.POST
	if not Subscriber.objects.filter(sid = delete_details['name']).delete():
		text = 'Subscriber Deleted Successfully'
		t = loader.get_template('success.html')
		c = RequestContext(request , { 'text' : text })
		return HttpResponse(t.render(c))
	return HttpResponse('Error While Deleting. Try again')

# Create your views here.

