from django.conf.urls import patterns, url
from time_engine import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^ajax/', views.ajax, name='ajax'),
        # /options/
        url(r'^options/$', views.options, name='options'),
        # /engine/
        url(r'^engine/$', views.engine, name='engine'),
        # /results/
        url(r'results/$', views.results, name='results'),
        # dom
        url(r'dom/$', views.dom, name='dom'),
        url(r'jsexample/$', views.jsexample, name='jsexample'),
        )