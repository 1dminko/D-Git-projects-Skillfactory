from django.urls import path
from .views import NewsList, NewsDetail, create_post, edit_post, delete_post, create_category, edit_category, delete_category


urlpatterns = [

   path('', NewsList.as_view()),
   path('<int:pk>', NewsDetail.as_view()),
   path('create/', create_post, name= 'post_create'),
   path('<int:pk>/edit/', edit_post, name= 'post_edit'),
   path('<int:pk>/delete/', delete_post, name= 'post_delete'),
   path('create/', create_post, name= 'post_create'),
   path('<int:pk>/edit/', edit_category, name= 'category_edit'),
   path('<int:pk>/delete/', delete_category, name= 'category_delete'),
]