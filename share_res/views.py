from django.http import HttpResponse


def index(request):
  return HttpResponse('index')


def restaurant_detail(request):
  return HttpResponse('restaurant_detail')


def create_restaurant(request):
  return HttpResponse('create_restaurant')


def create_category(request):
  return HttpResponse('create_category')
