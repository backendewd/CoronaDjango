from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('country/', views.country),
    path('gejala/', views.gejala),
    re_path(r'^country/(?P<country_requested>[\w|\W]+)/$', views.countryHome),
]