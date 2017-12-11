from django.conf.urls import *
from .googleauth.views import login, callback, logout
urlpatterns = [
    url(r'^login/$', login, name='googleauth_login'),
    url(r'^callback/$', callback, name='googleauth_callback'),
    url(r'^logout/$', logout, name='googleauth_logout'),
]
