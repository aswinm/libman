from django.shortcuts import render_to_response,get_object_or_404,render
from django.template import Context, RequestContext,loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from models import Auth
from forms import LoginForm
authenticated  = 0
def index(request):
	global authenticated
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			details = Auth.objects.create( 
					username = form.cleaned_data['username'],
					passwd = form.cleaned_data['password'],
					)
			dbdet = Auth.objects.get(pk = 1)
			if dbdet.username == details.username and dbdet.passwd == details.passwd:
				authenticated = 1
				return HttpResponseRedirect('welcome/')
			else:
				return HttpResponse("Sorry! Wrong call")
		else:
			authenticated = 0
			form = LoginForm()
			context = RequestContext(request)
			return render_to_response('login_page.html',{ 'form': form}, context)
	else:
		authenticated = 0
		form = LoginForm()
		context = RequestContext(request)
		return render_to_response('login_page.html',{ 'form': form}, context)
def welcome(request):
	t=loader.get_template('welcome.html')
 	c= RequestContext(request)	
	return HttpResponse(t.render(c))
def if_authenticated():
	return authenticated 
# Create your views here.
