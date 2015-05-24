__author__ = 'omr24'

from django.conf.urls import patterns, include, url
import kullanici.views

urlpatterns = patterns('kullanici.views',
    url(r'^giris', 'giris_formu'),
    url(r'^kayit', 'kayit_ekle'),
    url(r'^index', 'anasayfa'),


)