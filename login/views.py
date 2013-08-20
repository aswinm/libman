from django.shortcuts import render_to_response , render , get_object_or_404
from django.template import loader, Context , RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from models import Auth
from forms import LoginForm

authenticated = 0

def index(request):
	global authenticated
	form = LoginForm(request.POST)
	if request.method == 'POST' and form.is_valid():
		details = Auth.objects.create(
			username = form.cleaned_data['username'],
			passwd = form.cleaned_data['password'],
			)
		userdet = Auth.objects.get(pk=1)
		if userdet.username == details.username and details.passwd == userdet.passwd:
			authenticated = 1
			return HttpResponseRedirect('welcome/')
		else:
			return HttpResponse('Sorry! Wrong Call')
	else:
		authenticated = 0
		t =  loader.get_template('login_page.html')
		c = RequestContext(request, { 'form' : form })
		return HttpResponse(t.render(c))

def welcome(request):
	t = loader.get_template('welcome.html')
	c = RequestContext(request)
	return HttpResponse(t.render(c))

def if_authenticated():
	return authenticated



