from flask import Blueprint, render_template

err_blueprint = Blueprint(
    'err_pages',
    __name__,
    template_folder='templates')


@err_blueprint.app_errorhandler(404)
def err_404(err):
    return render_template(
        'error.html',
        err=err,
        error_code='404',
        message="Oops, we can't find that page..."), 404
