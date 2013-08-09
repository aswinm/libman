from django.conf.urls import url, patterns
from subscribers import views

urlpatterns = patterns('',
		url(r'login/welcome/subscribers/?$', views.index),
		url(r'login/welcome/subscribers/add/?$', views.addSub),
		)

