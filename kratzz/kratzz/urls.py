#coding=utf-8
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

##from applications.core import views

admin.autodiscover()

urlpatterns = [
    ##url(r'^$', views.home),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', admin.site.urls),
    ##url(r'^rosetta/', include('rosetta.urls')),
    url(r'^docs/', include('rest_framework_docs.urls')),
]
