from flask import render_template
from app import create_app, db

app = create_app()

@app.get('/')
def home():
    return render_template('home.html')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
