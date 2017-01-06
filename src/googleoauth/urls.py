from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='googleoauth_login'),
    url(r'^callback/$', views.callback, name='googleoauth_callback'),
    url(r'^logout/$', views.logout, name='googleoauth_logout'),
]
