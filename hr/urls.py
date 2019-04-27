from django.conf.urls import url
from .views import *
urlpatterns=[
    url(r'^login/$',login),
    url(r'^fang_in/$',fang_in),
    url(r'^fang_info/$',fang_info)
]