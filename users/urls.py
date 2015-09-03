from django.conf.urls import url,patterns
from users import views

urlpatterns = patterns('',
        url(r'^$',views.index),
        url(r'^logout/?$',views.logoff),
        url(r'^login/?$',views.logon),
        url(r'^register/?$',views.register),
        )
