from django.urls import path
from .views import PostList, PostCreate, PostDetail, PostUpdate, PostDelete, CategoryListView, subscribe

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name = 'post_add'), #news_single_create(used to be)
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

   path('categories/<int:pk>', CategoryListView.as_view(), name = 'category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name = 'subscribe'),


]