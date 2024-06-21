from flask import Flask
from .config import Config
from .models import db
from flask_migrate import Migrate
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(main)

    return app
