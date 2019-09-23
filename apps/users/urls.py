from django.urls import path, re_path
from django.conf.urls import include
# from rest_framework import routers, serilizers, viewsets
from apps.users.views import CustomAuthToken

urlpatterns = [
    re_path(r'^login', CustomAuthToken.as_view()),
]
