from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
path('home/',views.home,name='home'),
path('transfer/',views.transfer,name='transfer'),
path('success/',views.check,name='check'),
path('customers/',views.customers,name='customers'),
path('history/',views.history,name='history'),
path('check/',views.valid,name='valid'),

]

urlpatterns += staticfiles_urlpatterns()