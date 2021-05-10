import requests

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    url_for)
from werkzeug.wrappers import Response

from utils import is_staging, admin_auth
from .forms import APIForm

core_blueprint = Blueprint(
    'core',
    __name__,
    template_folder='templates')

url = 'www.example.com'


@core_blueprint.route('/', methods=['GET', 'POST'])
def index() -> Response:
    if is_staging() and not admin_auth():
        return redirect(url_for('admin.login_admin'))
    return render_template('index.html')


@core_blueprint.route('/hashing', methods=['GET', 'POST'])
def hashing() -> Response:
    if is_staging() and not admin_auth():
        return redirect(url_for('admin.login_admin'))
    form = APIForm()
    index_args = {'title': 'Scramble API', 'form': form}
    if form.validate_on_submit():
        res = requests.post(url, data={
            'hashing': form.hashing.data,
            'text': form.text.data,
            'file': form.file_upload.data
        })
        if res.status_code == 200:
            flash(res.message, 'message')
            return render_template('results.html')
        else:
            flash(res.message, 'warning')
            return render_template('hash.html', **index_args)
    return render_template('hash.html', **index_args)


@core_blueprint.route('/encryption', methods=['GET', 'POST'])
def encryption() -> Response:
    if is_staging() and not admin_auth():
        return redirect(url_for('admin.login_admin'))
    form = APIForm()
    index_args = {'title': 'Scramble API', 'form': form}
    if form.validate_on_submit():
        res = requests.post(url, data={
            'encryption': form.encryption.data,
            'text': form.text.data,
            'file': form.file_upload.data
        })
        if res.status_code == 200:
            flash(res.message, 'message')
            return render_template('results.html')
        else:
            flash(res.message, 'warning')
            return render_template('encrypt.html', **index_args)
    return render_template('encrypt.html', **index_args)
