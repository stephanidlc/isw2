from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
  path('', Login.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
]
