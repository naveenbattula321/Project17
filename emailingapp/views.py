from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random
def otp_send(request):
    subject = 'lokesh it otp'
    email_message = str(random.randint(100000,999999))
    From_mail = settings.EMAIL_HOST_USER
    to_list = ['battulanaveen261@gmail.com']
    send_mail(subject,email_message,From_mail,to_list,fail_silently=True)
    return HttpResponse("otp send successfully")
