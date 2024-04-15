from django.core.mail import send_mail

def SendMail(data):
    print(data)
    send_mail(data['subject'], data['message'], 'admin@codeanalyzer.com', [data['mail']], fail_silently=False)