from django.shortcuts import render,render_to_response
from login import views
from  django.template import Context, RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect
from models import LendBook


def index(request):
    if not views.if_authenticated():
        t = loader.get_template('login.html')
        c = RequestContext(request)
        return HttpResponse(t.render(c))
    t = loader.get_template('transactions_index.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))

# Create your views here.
