from flask import Flask
from .config import Config
from .models import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate = Migrate(app, db)

    from .routes import main
    from .api import api_bp

    app.register_blueprint(main)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
