import json
import hashlib
import requests
from django.conf import settings


def send_sms(text, phone):
    if settings.TESTING or (settings.DEBUG and not settings.SMS_TOKEN):
        return

    phone = str(phone)
    if phone.startswith(('+998', '998')):
        send_sms_eskiz(text, phone)
    else:
        send_sms_epochta(text, phone)


def send_sms_eskiz(text, phone):
    url = 'http://sms.eskiz.uz:8080/secure/send'
    data = json.dumps({'to': phone, 'from': '4546', 'content': text, 'dlr-level': 2})

    requests.post(headers={'Authorization': f'Basic {settings.SMS_TOKEN}'}, url=url, data=data).json()


def send_sms_epochta(text, phone):
    public_key = '0959c285b8e394bb1ea212ce61b08f3c'
    private_key = '50bd8dc3ca2d684723345265b00ef5c8'

    def calc_control_sum(_params):
        _params['key'] = public_key
        _params['version'] = '3.0'
        _params['action'] = 'sendSMS'

        control_str = ''
        for key in sorted(_params):
            control_str += _params[key]

        control_str += private_key

        return hashlib.md5(control_str.encode('utf-8')).hexdigest()

    url = 'http://api.atompark.com/api/sms/3.0/sendSMS'
    _data = {
        'sender': 'Info',
        'text': text,
        'phone': phone,
        'datetime': '',
        'sms_lifetime': '0'
    }
    control_sum = calc_control_sum(_data)

    data = {
        'key': public_key,
        'sum': control_sum,
        'sender': _data['sender'],
        'text': text,
        'phone': phone,
        'datetime': _data['datetime'],
        'sms_lifetime': _data['sms_lifetime']
    }

    requests.post(url=url, data=data).json()
