from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('restaurant_detail/delete', views.delete_restaurant_delete, name='delete_restaurant_delete'),
  path('restaurant_detail/<str:res_id>', views.restaurant_detail, name='restaurant_detail_page'),
  path('restaurant_detail/update_page/update', views.update_restaurant_update, name='update_restaurant_update'),
  path('restaurant_detail/update_page/<str:res_id>', views.update_restaurant, name='update_restaurant_page'),
  path('create_restaurant/', views.create_restaurant, name='create_restaurant_page'),
  path('create_restaurant/create', views.create_restaurant_create, name='create_restaurant_create'),
  path('create_category/', views.create_category, name='create_category_page'),
  path('create_category/create', views.create_category_create, name='create_category_create'),
  path('create_category/delete', views.create_category_delete, name='create_category_delete'),
]
