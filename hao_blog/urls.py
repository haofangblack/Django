"""hao_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from article import views as learn_views

urlpatterns = [
	url(r'^test/$', learn_views.test, name='test1'),
	url(r'^(\d+)/$', learn_views.detail, name='detail'),
	url(r'^$', learn_views.home, name='home'),
	url(r'^add1/(\d+)/(\d+)/$', learn_views.add1, name='add1'),
    url(r'^admin/', include(admin.site.urls)),
]
