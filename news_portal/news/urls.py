from django.urls import path
from .views import NewsList, NewsDetail, CreateNews, NewsUpdate, delete_post, create_category, edit_category, \
   delete_category
from django.contrib import admin
#from django.urls import include       create_post


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', NewsDetail.as_view()),
   #path('create/', create_post, name= 'post_create'),
   path('create/', CreateNews.as_view(), name= 'news_create'),
   path('<int:pk>/edit/', NewsUpdate.as_view(), name= 'edit_post'),
   #path('<int:pk>/edit/', edit_post, name= 'post_edit'),
   #path('<int:pk>/delete/', delete_post, name= 'post_delete'),
   #path('create/', create_post, name= 'post_create'),
   path('<int:pk>/edit/', edit_category, name= 'category_edit'),
   path('<int:pk>/delete/', delete_category, name= 'category_delete'),
]