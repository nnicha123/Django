# from django.contrib import admin
from django.urls import path,re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = 'articles'

urlpatterns = [
    path('',views.article_list,name="list"),
    re_path(r'^create/$',views.article_create,name="create"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_details,name="detail"),
]
