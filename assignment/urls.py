from django.conf.urls import url,patterns
from assignment import views

urlpatterns = patterns('',
        url(r'assignments/?$',views.assignments),
        url(r'^assignments/(?P<aid>\d+)/?$',views.assignment),
        url(r'assignments/add/?$',views.addassignment),
        url(r'^assignments/edit/(?P<aid>\d+)/?$',views.addassignment),
        url(r'^assignments/delete/(?P<aid>\d+)/?$',views.deleteassignment),
        url(r'^submit/?$',views.submit),
        )
