from django.contrib import admin
from django.urls import path, include
from . import views

app_name='mainapp'
urlpatterns = [
    path('blogpost/', views.blogpost, name='blogpost'),
    path('add_blog_details/',views.add_blog_details,name='add_blog_details'),
    path('view/',views.view_blog_details,name='view_blog_details'),
    path('edit/<int:blog_id>',views.edit_blog_details,name='edit_blog_details'),
    path('delete/<int:blog_id>',views.delete_blog_details,name='delete_blog_details'),
    path('comment_list/', views.comment_list, name='comment_list'),
]
