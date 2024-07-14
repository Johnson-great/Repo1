from flask import Blueprint, redirect, request, render_template, url_for
from flask_login import login_user, logout_user, login_required, current_user
from models.user import User, db


auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        user = User(email=email, username=username)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        login_user(user)
        return redirect(url_for('views.admin.dashboard'))
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.verify_password(password):
            login_user(user)
            return redirect(url_for('views.admin.dashboard'))
        else:
            error = 'Invalid username or password'
    else:
        error = None
    return render_template('login.html', error=error)

# Logout view
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
