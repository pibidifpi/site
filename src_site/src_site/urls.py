from django.conf.urls import patterns, include, url
from src_site.views import eventoIndex,eventoSobre


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'src_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^uploads/', include(admin.site.urls)),
    url(r'^evento/$', eventoIndex, name='index'),
    url(r'^informacoes/$', eventoSobre, name='sobre'),
)
