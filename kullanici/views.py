from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import *
from django.template import RequestContext
from kullanici.models import *
from kullanici.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

def anasayfa(request):
	return render_to_response('index.html', locals())

def giris_formu(request):
 if request.GET.get('cikis'):
  logout(request)
  return HttpResponseRedirect('/index/')

 if request.POST.get('giris'):
  giris_formu = AuthenticationForm(data=request.POST)
  if giris_formu.is_valid():
   kullaniciadi = request.POST['username']
   sifre = request.POST['password']
   kullanici = authenticate(username=kullaniciadi,password=sifre)
   if kullanici is not None:
    if kullanici.is_active:
     login(request,kullanici)
 else:
  giris_formu = AuthenticationForm()

 return render_to_response('giris.html',locals(),context_instance = RequestContext(request))


def kayit_ekle(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        member_user_auth = User.objects.create_user(username, email, password)
        member_user_auth.save()


        return HttpResponseRedirect('/kayit/')
    else:
        return render_to_response('kayit.html', context_instance=RequestContext(request))

