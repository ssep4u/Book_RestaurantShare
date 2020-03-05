from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse

from share_res.models import Restaurant


def send_email(request):
  checked_res_list = request.POST.getlist('checks')
  input_receiver = request.POST['input_receiver']
  input_title = request.POST['input_title']
  input_content = request.POST['input_content']
  restaurants = []
  for checked_res_id in checked_res_list:
    restaurants.append(Restaurant.objects.get(id=checked_res_id))
  content = {'input_content': input_content, 'restaurants': restaurants}
  msg_html = render_to_string('send_email/email_format.html', content)
  msg = EmailMessage(subject=input_title, body=msg_html, from_email=settings.EMAIL_HOST_USER,
                     bcc=input_receiver.split(','))
  msg.content_subtype = 'html'
  msg.send()
  return HttpResponseRedirect(reverse('index'))
