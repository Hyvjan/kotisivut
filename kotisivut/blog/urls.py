from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
	url(r'^$', views.posts_list, name='posts_list'),
	url(r'add_post/', views.add_post, name='add_post'),
	url(r'delete_post/(?P<pk>\d+)', views.delete_post, name='delete_post'),


]