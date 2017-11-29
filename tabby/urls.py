from django.conf.urls import url
from . import views

app_name = 'tabby'
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
]