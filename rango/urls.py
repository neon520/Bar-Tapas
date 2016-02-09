from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_bar/$', views.add_bar, name='add_bar'),
    url(r'^add_tapa/(?P<bar_nombre_slug>[\w\-]+)/$', views.add_tapa, name='add_tapa'),
    url(r'^bar/(?P<bar_nombre_slug>[\w\-]+)/$', views.bar, name='bar'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^reclama_datos/$', views.reclama_datos, name='reclama_datos'),
    url(r'^like_tapa/$', views.like_tapa, name='like_tapa'),
    )  # New!
