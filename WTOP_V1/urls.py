from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
   url(r'^admin/', include(admin.site.urls)),
    url(r'', include('kullanici.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'giris.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': 'index'}),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()