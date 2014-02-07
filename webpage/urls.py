from django.conf.urls import patterns, include, urls
from webpage import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home')

)