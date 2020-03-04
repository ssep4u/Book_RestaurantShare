from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Category, Restaurant


def index(request):
  categories = Category.objects.all()
  restaurants = Restaurant.objects.all()
  content = {'categories': categories, 'restaurants': restaurants}
  return render(request, 'share_res/index.html', content)


def delete_restaurant_delete(request):
  res_id = request.POST['restaurant_id']
  restaurant = Restaurant.objects.get(id=res_id)
  restaurant.delete()
  return HttpResponseRedirect(reverse('index'))


def restaurant_detail(request, res_id):
  restaurant = Restaurant.objects.get(id=res_id)
  content = {'restaurant': restaurant}
  return render(request, 'share_res/restaurant_detail.html', content)


def update_restaurant(request, res_id):
  categories = Category.objects.all()
  restaurant = Restaurant.objects.get(id=res_id)
  content = {'categories': categories, 'restaurant': restaurant}
  return render(request, 'share_res/update_restaurant.html', content)


def update_restaurant_update(request):
  restaurant_id = request.POST['restaurant_id']
  change_category_id = request.POST['restaurant_category']
  change_category = Category.objects.get(id=change_category_id)
  change_name = request.POST['restaurant_name']
  change_link = request.POST['restaurant_link']
  change_content = request.POST['restaurant_content']
  change_keyword = request.POST['restaurant_keyword']
  before_restaurant = Restaurant.objects.get(id=restaurant_id)
  before_restaurant.category = change_category
  before_restaurant.restaurant_name = change_name
  before_restaurant.restaurant_link = change_link
  before_restaurant.restaurant_content = change_content
  before_restaurant.restaurant_keyword = change_keyword
  before_restaurant.save()
  return HttpResponseRedirect(reverse('restaurant_detail_page', kwargs={'res_id': restaurant_id}))


def create_restaurant(request):
  categories = Category.objects.all()
  content = {'categories': categories}
  return render(request, 'share_res/create_restaurant.html', content)


def create_restaurant_create(request):
  category_id = request.POST['restaurant_category']
  category = Category.objects.get(id=category_id)
  name = request.POST['restaurant_title']
  link = request.POST['restaurant_link']
  content = request.POST['restaurant_content']
  keyword = request.POST['restaurant_keyword']
  new_restaurant = Restaurant(category=category, restaurant_name=name, restaurant_link=link, restaurant_content=content,
                              restaurant_keyword=keyword)
  new_restaurant.save()
  return HttpResponseRedirect(reverse('index'))


def create_category(request):
  categories = Category.objects.all()
  content = {'categories': categories}
  return render(request, 'share_res/create_category.html', content)


def create_category_create(request):
  category_name = request.POST['category_name']
  new_category = Category(category_name=category_name)
  new_category.save()
  return HttpResponseRedirect(reverse('index'))


def create_category_delete(request):
  category_id = request.POST['category_id']
  delete_category = Category.objects.get(id=category_id)
  delete_category.delete()
  return HttpResponseRedirect(reverse('create_category_page'))
