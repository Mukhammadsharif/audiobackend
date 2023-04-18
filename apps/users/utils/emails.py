from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string


def send_verification_email(request, user, is_mobile=False):
    device = 'mobile' if is_mobile else 'desktop'
    url = f'{settings.FRONTEND_DOMAIN}/confirm/{user.confirmation_code}?device={device}'

    text = render_to_string('confirm_email.html', {'user': user, 'url': url, 'settings': settings}, request)
    subject = _('Activate your account at {}').format(settings.COMPANY_NAME)
    user.email_user(subject, text, html_message=text)


def send_message_email(title, body, user):
    user.email_user(title, body)


def send_reset_link_email(request, reset, user):
    url = '{}?reset_password_key={}'.format(settings.FRONTEND_DOMAIN, reset.key)
    text = render_to_string('reset_password.html', {'user': user, 'url': url, 'settings': settings}, request)
    subject = _('Restore your password for {}').format(settings.COMPANY_NAME)
    user.email_user(subject, text, html_message=text)
