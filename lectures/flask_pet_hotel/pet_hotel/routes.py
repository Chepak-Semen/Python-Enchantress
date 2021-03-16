from flask import Blueprint, request


check_in_bp = Blueprint('chek-in', __name__, url_prefix='/check-in')


@check_in_bp.route('/', methods=['POST'])
@check_in_bp.route('', methods=['POST'])
def check_in():
    return 'success'
