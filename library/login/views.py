from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from models import Auth
def index(request):
	return render(request,'login_page.html')
x=''
def process(request):
	global x
	x=request.GET
	return HttpResponseRedirect('login/thanks/') 
def thanks(request):
	log = Auth.objects.get(pk=1)
	if log.username == x['uname'] and log.passwd == x['passwd']:
		return HttpResponse("Successfully Logged In")
	return HttpResponse("User Details Do not Match") 
# Create your views here.
