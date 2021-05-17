import os
import requests
from typing import Dict
from flask import flash, session
from werkzeug.wrappers import Response

url = os.environ['API_URL']


def is_staging() -> bool:
    """
    Check to see if the app is running with the Staging coniguration

    :return: boolean
    """
    return os.environ['APP_SETTINGS'] == 'config.StagingConfig'


def admin_auth() -> bool:
    """
    Check if the admin has authorised themselves by checking the
    current session for the ADMIN_SESSION value

    :return: boolean
    """
    admin_session = session.get('ADMIN_SESSION')
    if not admin_session:
        flash('Admin access only', 'warning')
        return False
    return True


def make_api_request(type, endpoint, data) -> Response:
    """
    Makes an API request and returns the data from the
    response as JSON

    :param type: a HTTP verb
    :param endpoint: the API endpoint to hit
    :param data: the data to send
    """
    if type == 'get':
        res = requests.get(f"{url}/{endpoint}")
    elif type == 'post':
        res = requests.post(f"{url}/{endpoint}", **data)
    elif type == 'put':
        res = requests.put(f"{url}/{endpoint}", **data)
    elif type == 'delete':
        res = requests.delete(f"{url}/{endpoint}", **data)
    return res
