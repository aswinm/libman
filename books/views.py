from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, RequestContext, loader
from models import Book
from forms import BookAddForm
from login import views
from transactions.models import LendBook

flag = 0

def index(request):
	if not views.if_authenticated():
		t = loader.get_template('login.html')
		c = RequestContext(request)
		return HttpResponse(t.render(c))
	t = loader.get_template('books_index.html')
	c = RequestContext(request)
	return HttpResponse(t.render(c))

def add(request):
	if not views.if_authenticated():
		t = loader.get_template('login.html')
		c = RequestContext(request)
		return HttpResponse(t.render(c))

	form = BookAddForm(request.POST)
	if request.method == 'POST' and form.is_valid():
        	book_details = Book.objects.create(
				bid = form.cleaned_data['bid'],
				name = form.cleaned_data['bname'],
				author = form.cleaned_data['author'],
				Totbooks = form.cleaned_data['TotBooks'],
				Avlbooks = form.cleaned_data['AvlBooks'],
				)
		book_details.save()
		t = loader.get_template('success.html')
		text = 'Book Added Successfully'
		c = RequestContext(request, { 'text' : text } )	
		return HttpResponse(t.render(c))
	else:
		text = 'Add New Book'
		t = loader.get_template('add.html')
		context = RequestContext(request, { 'text' :text , 'form': form})
		return HttpResponse(t.render(context))

def search(request):
	if not views.if_authenticated():
		t = loader.get_template('login.html')
		c = RequestContext(request)
		return HttpResponse(t.render(c))
	t = loader.get_template('search_book.html')
	c = RequestContext( request )
	return HttpResponse(t.render(c))

def searchdelete(request):
	if not views.if_authenticated():
		t = loader.get_template('login.html')
		c = RequestContext(request)
		return HttpResponse(t.render(c))
	global flag
	flag = 1
	t = loader.get_template('search_book.html')
	c = RequestContext( request )
	return HttpResponse(t.render(c))

def display(request):
	if not views.if_authenticated():
		t = loader.get_template('login.html')
		c = RequestContext(request)
		return HttpResponse(t.render(c))
	global flag
	search_details = request.POST
	print search_details
	result = Book.objects.filter(name__contains = search_details['name'])
 	print len(result)
	if not result:
		return HttpResponse("Book Not Found")
	t = loader.get_template('book_display_delete.html')
	c = RequestContext(request , { 'j' : flag , 'booklist' : result })
	flag = 0
	return HttpResponse(t.render(c))

def delete(request):
	if not views.if_authenticated():
		t = loader.get_template('login.html')
		c = RequestContext(request)
		return HttpResponse(t.render(c))
	delete_details  = request.POST
	if not Book.objects.filter(bid = delete_details['bname']).delete():
		text = 'Book Entry Deleted Successfully'
		t = loader.get_template('success.html')
		c = RequestContext(request , { 'text' : text } )
		return HttpResponse(t.render(c))
	return HttpResponse('Error While deleting')

def bookdetails(request, book_id):
	if not views.if_authenticated():
		t = loader.get_template('login.html')
		c = RequestContext(request)
		return HttpResponse(t.render(c))
	book_details = Book.objects.get(pk = book_id)
	book_history = LendBook.objects.filter(bid = book_id)
	t = loader.get_template('book_details.html')
	c = RequestContext(request , { 'book' : book_details , 'history' : book_history } )
	return HttpResponse(t.render(c))


	
# Create your views here.
