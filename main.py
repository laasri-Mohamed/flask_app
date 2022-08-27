from flask import Blueprint, render_template 
from flask_login import login_required, current_user
#from auth import auth

main = Blueprint('main', __name__)
#main.register_blueprint(auth)
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/generation')
def generation():
    return render_template('generation.html')

@main.route('/history')
def history():
    return render_template('history.html')