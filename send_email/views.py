import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.http import HttpResponseRedirect
from django.urls import reverse

from share_res.models import Restaurant


def send_email(request):
  checked_res_list = request.POST.getlist('checks')
  input_receiver = request.POST['input_receiver']
  input_title = request.POST['input_title']
  input_content = request.POST['input_content']
  mail_html = '<html><body>'
  mail_html += '<h1>맛집 공유</h1>'
  mail_html += '<p>' + input_content + '<br>'
  mail_html += '발신자님께서 공유하신 맛집은 다음과 같습니다.</p>'
  for checked_res_id in checked_res_list:
    restaurant = Restaurant.objects.get(id=checked_res_id)
    mail_html += '<h2>' + restaurant.restaurant_name + '</h2>'
    mail_html += '<h4>* 관련 링크</h4><p>' + restaurant.restaurant_link + '</p><br>'
    mail_html += '<h4>* 상세 내용</h4><p>' + restaurant.restaurant_content + '</p><br>'
    mail_html += '<h4>* 관련 키워드</h4><p>' + restaurant.restaurant_keyword + '</p><br>'
    mail_html += '<br>'
  mail_html += '</body></html>'

  # smtp using
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.login('ssep4u@gmail.com', 'gmail패스워드')
  msg = MIMEMultipart('alternative')
  msg['Subject'] = input_title
  msg['From'] = 'ssep4u@gmail.com'
  msg['To'] = input_receiver
  mail_html = MIMEText(mail_html, 'html')
  msg.attach(mail_html)
  print(msg['To'], type(msg['To']))
  server.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
  server.quit()

  return HttpResponseRedirect(reverse('index'))
