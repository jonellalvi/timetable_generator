from django.conf.urls import patterns, url
from time_engine import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        # /options/
        url(r'^options/$', views.options, name='options'),
        # /engine/
        url(r'^engine/$', views.engine, name='engine'),
        # /results/
        url(r'results/$', views.results, name='results')
        )