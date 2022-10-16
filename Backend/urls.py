from django.urls import re_path
from Backend import views

urlpatterns=[
    re_path(r'^$', views.projectAPI),
    re_path(r'^([0-9]+)$', views.projectAPI)
]