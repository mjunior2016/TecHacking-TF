"""techacking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from core.views import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^index', index),
    url(r'^cursosgraduacao', cursosgraduacao),
    url(r'^cursospos', cursospos),
    url(r'^cursoscertificacao', cursoscertificacao),
    url(r'^graduacaosistemas', graduacaosistemas),
    url(r'^graduacaoredes', graduacaoredes),
    url(r'^graduacaogames', graduacaogames),
    url(r'^graduacaohacking', graduacaohacking),
    url(r'^contato', contato),
    url(r'^login', login),
    url(r'^loginaluno', loginaluno),
    url(r'^loginprofessor', loginprofessor),
    url(r'^logincoordenador', logincoordenador),
    url(r'^matriculese', matriculese),
    url(r'^login', login),
    url(r'^logout', logout),
]
