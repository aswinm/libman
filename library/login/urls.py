from django.conf.urls import patterns,url
from login import views

urlpatterns=patterns('',
		url(r'^loginr/?$',views.process),
		url(r'^loginr/login/thanks/?$',views.thanks),
		url(r'^login/?$',views.index, name="index"),
	)
