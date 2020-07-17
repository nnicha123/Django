# from django.contrib import admin
from django.urls import path,re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.article_list),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_details),
]
urlpatterns += staticfiles_urlpatterns()