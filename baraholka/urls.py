# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from www import views
from www.forms import LoginForm




urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', views.main),
                       url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemap},
                            name='django.contrib.sitemaps.views.sitemap'),  # Треба розібратись із сайтмапом і нормально налаштувати
                       url(r'^registration/$', views.registration, {
                            'template_name': 'registration.html',
                            'autologin': True,
                            'callback': None
                            }, name='registration'),
                       url(r'^login/$', 'django.contrib.auth.views.login', {
                            'authentication_form': LoginForm,
                            'template_name':'login.html',
                            }, name='login'),
                       (r'^logout/$', views.logout),
                       url(r'^category=(?P<cat>\d+)/$', views.main),
                       url(r'^view/(?P<tovar_id>\d+)/$', views.tovar),                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':'./static/'}),
                       url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':'./media/'}),
)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)