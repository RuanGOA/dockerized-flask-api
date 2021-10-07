from app.routes.status_route import status
from app.routes.hi_route import hi

def create_routes(app):
    app.register_blueprint(status, url_prefix='/status')
    app.register_blueprint(hi, url_prefix='/hi')
