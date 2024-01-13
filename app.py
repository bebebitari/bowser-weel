import os
from flask import Flask, render_template
from werkzeug.utils import quote
import importlib.metadata
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
# Використовуйте PORT, який задається Heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)