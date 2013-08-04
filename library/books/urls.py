from django.conf.urls import patterns,url
from books import views

urlpatterns = patterns('',
		url(r'login/welcome/books/?$',views.index),
		url(r'login/welcome/books/add/?$', views.add),
		)

