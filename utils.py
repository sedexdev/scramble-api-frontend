import os
from flask import flash, redirect, session, url_for


def check_is_staging():
    if os.environ['APP_SETTINGS'] == 'config.StagingConfig':
        admin_username = session.get('ADMIN_USERNAME')
        if not admin_username:
            flash('Admin access only', 'warning')
            return redirect(url_for('admin.login_admin'))
