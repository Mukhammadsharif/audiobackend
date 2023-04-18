import requests
from rest_framework.utils import json

from core.utils.helpers import split_array


def send_notification(data):
    newData = [data] if len(data) < 101 else []

    if isinstance(data, dict):
        newData = [data]

    if len(data) > 10:
        newData = split_array(data, 100)

    for i in newData:
        requests.post(
            "https://exp.host/--/api/v2/push/send",
            json.dumps(i),
            headers={
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate',
                'content-type': 'application/json',
            }
        ).json()
