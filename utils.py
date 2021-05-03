import os
from flask import flash, session


def is_staging() -> bool:
    return os.environ['APP_SETTINGS'] == 'config.StagingConfig'


def admin_auth() -> bool:
    admin_username = session.get('ADMIN_USERNAME')
    if not admin_username:
        flash('Admin access only', 'warning')
        return False
    return True
