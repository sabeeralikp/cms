# from django.core.mail import EmailMultiAlternatives

# def send_mail_as_template():
#     subject, from_email, to = "New conference request from {send_user.first_name} {send_user.last_name}", "os.environ.get(NO_REPLY_MAIL)", "os.environ.get(ADMIN_EMAIL)"
#     text_content = "There is a new conference request"
#     html_content = "<p><b>Email:</b> {send_user.email}</p><p><b>Conference Name:</b> {serializer.data['title']}</p>"
#     msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()

from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk)
            + six.text_type(timestamp)
            + six.text_type(user.is_active)
        )


generate_token = TokenGenerator()
