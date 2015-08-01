from flask import render_template
from menu import menu

@menu.route('/')
def index():
    return render_template('index.html')
