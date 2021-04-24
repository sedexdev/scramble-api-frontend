import os
from flask import flash, session


def is_staging():
    if os.environ['APP_SETTINGS'] == 'config.StagingConfig':
        admin_username = session.get('ADMIN_USERNAME')
        if not admin_username:
            flash('Admin access only', 'warning')
        return True
    return False
