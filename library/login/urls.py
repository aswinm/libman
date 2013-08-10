from django.conf.urls import patterns,url
from login import views 
from books import views as v2

urlpatterns=patterns('',
		url(r'login/?$',views.index, name="index"),
		url(r'login/welcome/?$',views.welcome),
		url(r'Books/?/?$' , v2.index),
	)
