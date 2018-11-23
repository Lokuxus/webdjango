# CODE_HOME/mysite/hello/urls.py
# This is the urls.py file for the hello App

from django.conf.urls import url
import webapidjango.views

app_name = 'webapidjango'
urlpatterns = [
    url(r'^(?P<word>[A-Za-z]+)/$', webapidjango.views.helloview, name='webapidjango'),  # View url
]