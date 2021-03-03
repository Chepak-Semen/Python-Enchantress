from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    response = {'success'}
    return response, 200


@main.route('/profile')
@login_required
def profile():
    response = {f'success, name is {current_user.name}'}
    return response, 200
