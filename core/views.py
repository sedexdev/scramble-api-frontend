from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    url_for)
from utils import is_staging
from .forms import APIForm
import requests

core_blueprint = Blueprint(
    'core',
    __name__,
    template_folder='templates')

url = 'www.example.com'


@core_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if is_staging():
        return redirect(url_for('admin.login_admin'))
    form = APIForm()
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
        return render_template('index.html', title='Scramble API', form=form)
    return render_template('index.html', title='Scramble API', form=form)
