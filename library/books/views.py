from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, RequestContext, loader
from models import Book
from forms import BookAddForm
from login import views
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

	if request.method == 'POST':
		form = BookAddForm(request.POST)
		if form.is_valid():
			book_details = Book.objects.create(
					bid = form.cleaned_data['bid'],
					name = form.cleaned_data['bname'],
					author = form.cleaned_data['author'],
					Totbooks = form.cleaned_data['TotBooks'],
					Avlbooks = form.cleaned_data['AvlBooks'],
					)
			book_details.save()
			t = loader.get_template('success.html')
			c = RequestContext(request)	
			return HttpResponse(t.render(c))
		else:
			form = BookAdForm()
			text = 'Book Added Successfully'
			context = RequestContext(request, { 'text' :text })
			return render_to_response('add_book.html' , {'form': form }, context )

	else:
		form = BookAddForm()
		context = RequestContext(request)
		return render_to_response('add_book.html' , {'form': form }, context )

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
	
# Create your views here.
