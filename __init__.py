from .mystery_api import mystery_api_bp
from .mystery import mystery_bp


def register_routes(app):
    app.register_blueprint(mystery_api_bp)
    app.register_blueprint(mystery_bp)
  
