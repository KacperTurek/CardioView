from django.conf.urls import url
from . import views

urlpatterns = [
    # /signal/
    url(r'^$', views.index, name='index'),

    # /signal/mitdb/100
    #url(r'^plot/(?P<database_id>[0-9]+)/(?P<signal_display>[0-9]+)/$', views.signal_plot, name='signal_plot'),

    # /signal/plot
    url(r'^plot/$', views.signal_plot, name='signal_plot'),
]