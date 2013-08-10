from django.conf.urls import url, patterns
from subscribers import views

urlpatterns = patterns('',
		url(r'login/welcome/subscribers/?$', views.index),
		url(r'login/welcome/subscribers/add/?$', views.addSub),
		url(r'login/welcome/subscribers/search/?$', views.search),
		url(r'login/welcome/subscribers/delete/?$', views.searchdelete),
		url(r'login/welcome/subscribers/search/display/?$', views.display),
		url(r'login/welcome/subscribers/search/display/delete/?$', views.delete),
		)

