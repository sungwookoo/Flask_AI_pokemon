from flask import Blueprint, render_template

bp = Blueprint('feed', __name__, url_prefix='/')


@bp.route('/main')
def get_feed():
    return render_template('index.html')

