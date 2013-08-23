from django.shortcuts import render,render_to_response
from login import views
from  django.template import Context, RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect
from models import LendBook
from forms import LendingForm
from books.models import Book
from subscribers.models import Subscriber
import datetime


def index(request):
    if not views.if_authenticated():
        t = loader.get_template('login.html')
        c = RequestContext(request)
        return HttpResponse(t.render(c))
    t = loader.get_template('transactions_index.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))

def lend(request):
    if not views.if_authenticated():
        t = loader.get_template('login.html')
        c = RequestContext(request)
        return HttpResponse(t.render(c))
    form = LendingForm(request.POST)
    if request.method == "POST" and form.is_valid():
	bookid = Book.objects.get(pk = form.cleaned_data['bookid'])
	if bookid.Avlbooks<1:
		return HttpResponse('Book not available')
	subid = Subscriber.objects.get(pk = form.cleaned_data['subscriberid'])
	result = LendBook.objects.filter(bid = form.cleaned_data['bookid'], sid = form.cleaned_data['subscriberid'])
	for j in result:
		if j.returned == False:
			return HttpResponse('Subscriber already has a copy of this book')
	
        Date = datetime.datetime.now().date()
        lending = LendBook.objects.create(
            bid = bookid,
            sid = subid,
	    date = Date,
	    DueDate = Date + datetime.timedelta(days = 15),
	    returned = False,
        )
        lending.save()
	bookid.Avlbooks -= 1
	bookid.save()
	sub = Subscriber.objects.get(pk = form.cleaned_data['subscriberid'])
	sub.NoOfBooks += 1
	sub.save()
        t = loader.get_template('success.html')
	info = 'Due date: ' + str(lending.DueDate)
        text = 'Transaction successfully saved.'
	c = RequestContext(request , { 'text' :text , 'info' : info } )
        return HttpResponse(t.render(c))
    else:
        text = 'Lend Book'
        t = loader.get_template('add.html')
        c = RequestContext(request , { 'text' : text , 'form' : form })
        return HttpResponse(t.render(c))

def returnbook(request):
	if not views.if_authenticated():
		t = loader.get_template('login.html')
		c = RequestContext(request)
		return HttpResponse(t.render(c))
	form = LendingForm(request.POST)
	if request.method == "POST" and form.is_valid():
		print "POST"
		bookid = form.cleaned_data['bookid']
		subid = form.cleaned_data['subscriberid']
		book = Book.objects.get(pk = bookid)
		sub = Book.objects.get(pk = subid)
		date = datetime.datetime.now().date() 
		print "Values Assigned"
		details = LendBook.objects.filter(bid = bookid,sid = subid, returned = False)
		for j in details:
			j.returned = True
			j.ReturnDate = datetime.datetime.now().date()
			j.save()
		book.Avlbooks += 1
		book.save()
		sub_d = Subscriber.objects.get(pk = sub)
		sub_d.NoOfBooks -= 1
		sub_d.save()
        	t = loader.get_template('success.html')
        	text = 'Transaction successfully saved'
        	c = RequestContext(request , { 'text' :text } )
        	return HttpResponse(t.render(c))
	else:
		text = 'Return Book'
        	t = loader.get_template('add.html')
        	c = RequestContext(request , { 'text' : text , 'form' : form })
        	return HttpResponse(t.render(c))
	

# Create your views here.
