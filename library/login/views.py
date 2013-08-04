from django.shortcuts import render_to_response,get_object_or_404,render
from django.template import Context, RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from models import Auth
from forms import LoginForm
def index(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			details = Auth.objects.create( 
					username = form.cleaned_data['username'],
					passwd = form.cleaned_data['password'],
					)
			dbdet = Auth.objects.get(pk = 1)
			if dbdet.username == details.username and dbdet.passwd == details.passwd:
				return HttpResponseRedirect('thanks/')
			else:
				return HttpResponse("Sorry! Wrong call")
		else:
			form = LoginForm()
			context = RequestContext(request)
			return render_to_response('login_page.html',{ 'form': form}, context)
	else:
		form = LoginForm()
		context = RequestContext(request)
		return render_to_response('login_page.html',{ 'form': form}, context)
def thanks(request):
	return HttpResponse('Successfully Logged In')
# Create your views here.
