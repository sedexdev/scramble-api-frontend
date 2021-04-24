import os
from flask import flash, session


def is_staging():
    return os.environ['APP_SETTINGS'] == 'config.StagingConfig'


def admin_auth():
    admin_username = session.get('ADMIN_USERNAME')
    if not admin_username:
        flash('Admin access only', 'warning')
        return False
    return True
