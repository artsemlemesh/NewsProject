from django.urls import path
from .views import PostList, PostCreate, PostDetail, PostUpdate, PostDelete, CategoryListView, subscribe, Index
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),# cache_page(60) is off
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),#cache_page(300) is off because article cache is applied
   path('create/', PostCreate.as_view(), name = 'post_add'), #news_single_create(used to be)
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('index/', Index.as_view()),

   path('categories/<int:pk>', CategoryListView.as_view(), name = 'category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name = 'subscribe'),


]