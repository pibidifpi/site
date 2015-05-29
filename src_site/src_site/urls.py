from django.conf.urls import patterns, include, url
from src_site.views import *
from django.conf import settings


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'src_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^uploads/', include(admin.site.urls)),
    url(r'^$', EventoList.as_view(), name='eventoList'),
    url(r'^informacoes/$', EventoSobre.as_view(), name='eventoSobre'),
    url(r'^palestras/$',PalestraList.as_view() , name='palestraList'),
    url(r'^minicursos/$',MinicursoList.as_view() , name='minicursoList'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
)
