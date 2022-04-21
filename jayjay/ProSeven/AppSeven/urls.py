# from django.conf.urls import url
from django.urls import include, re_path
from AppSeven import views


app_name = 'AppSeven'

urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^user_login/$', views.user_login, name='user_login')
]