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
    form = APIForm()
    index_args = {'title': 'Scramble API', 'form': form}
    if form.validate_on_submit():
        res = requests.post(url, data={
            'service': form.serivce.data,
            'encryption': form.encryption.data,
            'hashing': form.hashing.data,
            'plaintext': form.plaintext.data,
            'text': form.text.data,
            'file': form.file_upload.data
        })
        if res.status_code == 200:
            flash(res.message, 'message')
        else:
            flash(res.message, 'warning')
        return render_template('index.html', **index_args)
    return render_template('index.html', **index_args)
