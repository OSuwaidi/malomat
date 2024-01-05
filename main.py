# بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ وبه نستعين

from flask import Flask, render_template
from datetime import timedelta
import numpy as np
import os

# Initialize app:
app = Flask(__name__, static_url_path='/static')

# App config:
app.secret_key = os.environ.get('OUR_SECRET', 'default_secret_key')
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
