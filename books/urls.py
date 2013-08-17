from django.conf.urls import patterns,url
from books import views

urlpatterns = patterns('',
		url(r'login/welcome/books/?$',views.index),
		url(r'login/welcome/books/add/?$', views.add),
		url(r'login/welcome/books/delete/?$', views.searchdelete),
		url(r'login/welcome/books/search/?$', views.search),
		url(r'login/welcome/books/delete/display/?$', views.display),
		url(r'login/welcome/books/search/display/?$', views.display),
		url(r'login/welcome/books/delete/display/del/?$', views.delete),
		)

