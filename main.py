# بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ وبه نستعين

from flask import Flask, request, render_template, redirect, url_for, session
from app_secrets import our_secret
from datetime import timedelta
import numpy as np

# Initialize app:
app = Flask(__name__, static_url_path='/static')

# App config:
app.secret_key = our_secret
app.permanent_session_lifetime = timedelta(minutes=30)


# Create landing page:
@app.get('/')
def homepage():
    return render_template("HOMEPAGE.html", random=np.random.choice)


# Create about page:
@app.get('/about')
def about():
    return render_template("ABOUT.html")


@app.get('/contact')
def contact():
    return "contact us"


if __name__ == '__main__':
    app.run(debug=True)
