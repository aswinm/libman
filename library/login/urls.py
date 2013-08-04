from django.conf.urls import patterns,url
from login import views

urlpatterns=patterns('',
		url(r'^login/?$',views.index, name="index"),
		url(r'^login/thanks/?$',views.thanks),
	)
