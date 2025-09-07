from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()  # <-- initialize mail here

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incident.db'
    app.config['MAIL_SERVER'] = 'smtp.example.com'   # replace with your SMTP config
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'your_email@example.com'
    app.config['MAIL_PASSWORD'] = 'your_password'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    db.init_app(app)
    mail.init_app(app)

    # import routes after initializing db and mail
    from . import routes
    app.register_blueprint(routes.bp)

    return app

