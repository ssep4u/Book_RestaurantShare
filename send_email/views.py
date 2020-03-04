from django.http import HttpResponse


def send_email(request):
  return HttpResponse('send_email')
