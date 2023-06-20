from django.core.mail import EmailMultiAlternatives

def send_mail_as_template():
    subject, from_email, to = "New conference request from {send_user.first_name} {send_user.last_name}", "os.environ.get(NO_REPLY_MAIL)", "os.environ.get(ADMIN_EMAIL)"
    text_content = "There is a new conference request"
    html_content = "<p><b>Email:</b> {send_user.email}</p><p><b>Conference Name:</b> {serializer.data['title']}</p>"
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()