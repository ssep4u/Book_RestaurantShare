from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('restaurant_detail/', views.restaurant_detail),
  path('create_restaurant/', views.create_restaurant),
  path('create_category/', views.create_category),
]
