from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^', include('data.urls')),
    url(r'^data/', include('data.urls')),
)


