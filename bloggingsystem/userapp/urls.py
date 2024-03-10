from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'userapp'
urlpatterns = [
    path('viewblogs', views.viewblogs, name='viewblogs'),
    path('blog_details_list', views.blog_details_list, name='blog_details_list'),
    path('submit_form/',views.submit_form,name='submit_form'),
    path('adduserprofile/',views.adduserprofile,name='adduserprofile'),
    path('open_blog/<int:blog_id>/',views.open_blog,name='open_blog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)