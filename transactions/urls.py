from django.conf.urls import url,patterns
import views

urlpatterns = patterns('',
                       url(r'login/welcome/transactions/?$', views.index),
		       url('login/welcome/transactions/lend/?$', views.lend),
		       url('login/welcome/transactions/return/?$', views.returnbook),
		       url('login/welcome/transactions/details/?$', views.transdet),
                       )
