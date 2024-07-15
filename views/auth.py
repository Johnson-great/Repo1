from flask import Blueprint, redirect, request, render_template, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from models.user import User, db


auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            user = User(email=email, username=username)
            user.set_password(password)

            db.session.add(user)
            db.session.commit()
        except Exception as exc:
            flash('could not add admin,  something went wrong', 'error')
            return render_template('register.html', current_user=current_user)

        flash(f'admin {username} successfully Registered', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', current_user=current_user)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.verify_password(password):
            login_user(user)
            flash(f"Welcome {user.__dict__.get('username')}", 'success')
            return redirect(url_for('views.student.get_students'))
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
    return redirect(url_for('views.auth.login'))
