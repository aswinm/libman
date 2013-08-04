from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, RequestContext, loader
from models import Book
from forms import BookAddForm

def index(request):
	t = loader.get_template('books_index.html')
	c = RequestContext(request)
	return HttpResponse(t.render(c))

def add(request):
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
			t = loader.get_template('book_save_success.html')
			c = RequestContext(request)	
			return HttpResponse(t.render(c))
		else:
			form = BookAdForm()
			context = RequestContext(request)
			return render_to_response('add_book.html' , {'form': form }, context )

	else:
		form = BookAddForm()
		context = RequestContext(request)
		return render_to_response('add_book.html' , {'form': form }, context )
# Create your views here.
