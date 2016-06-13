from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
	url(r'^$', views.posts_list, name='posts_list'),

]