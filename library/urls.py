from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
		# Examples:
		# url(r'^$', 'library.views.home', name='home'),
		# url(r'^blog/', include('blog.urls')),
		url(r'^admin/', include(admin.site.urls)),
		url(r'', include('login.urls')),
		url(r'', include('books.urls')),
		url(r'', include('subscribers.urls')),
       	url(r'', include('transactions.urls')),
		)

