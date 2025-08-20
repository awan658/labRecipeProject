from flask import render_template, Blueprint

browse_blueprint = Blueprint('browse_bp', __name__)

@browse_blueprint.route('/', methods=['GET'])
def browse():
    return render_template('browse.html')