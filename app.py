from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///snaplink.db'
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(500), nullable=False)
    short = db.Column(db.String(10), unique=True, nullable=False)

with app.app_context():
    db.create_all()

def generate_id():
    # Creates a random mix of letters and numbers
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        long_url = request.form['url']
        # Check if we already shortened this one
        existing = URL.query.filter_by(original=long_url).first()
        
        if existing:
            short_id = existing.short
        else:
            short_id = generate_id()
            new_entry = URL(original=long_url, short=short_id)
            db.session.add(new_entry)
            db.session.commit()
            
        short_url = request.host_url + short_id
    return render_template('index.html', short_url=short_url)

# The REDIRECT Engine
@app.route('/<short_id>')
def follow_link(short_id):
    link = URL.query.filter_by(short=short_id).first_or_404()
    return redirect(link.original)

if __name__ == "__main__":
    app.run(debug=True)