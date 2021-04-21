from flask import current_app, flash, redirect, session, url_for
from config import StagingConfig


def check_is_staging():
    if current_app.config == StagingConfig:
        admin_username = session.get('ADMIN_USERNAME')
        if not admin_username:
            flash('Admin access only', 'warning')
            return redirect(url_for('admin.admin'))
