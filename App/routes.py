from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('index.html')

@main.route('/page1')
def page1():
    return render_template('page1.html')

@main.route('/page2')
def page2():
    return render_template('page2.html')

def init_app(app):
    app.register_blueprint(main)
