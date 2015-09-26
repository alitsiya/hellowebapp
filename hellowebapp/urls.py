from django.conf.urls import patterns, include, url 
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'collection.views.index', name='home'),
    url(r'^about/$', 
        TemplateView.as_view(template_name='about.html'), name='about'), 
    url(r'^contact/$',
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    url(r'^things/(?P<slug>[-\w]+)/$', 'collection.views.thing_detail', name='thing_detail'),
    # new line we're adding!
    url(r'^things/(?P<slug>[-\w]+)/edit/$', 'collection.views.edit_thing', name='edit_thing'),
    url(r'^admin/', include(admin.site.urls)),
)