

from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('jscode', __name__, url_prefix='/jscode')

@bp.route('/', methods=('GET',"POST"))
def add():
    if request.method == 'POST':
        a = request.form.get('a')
        b = request.form.get('b')
        return jsonify(result=int(a)+int(b))
    return render_template('fetch.html')