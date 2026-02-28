from flask import Flask
from controllers.HomeController import blueprint_home
from extensions import db,migrate,swagger,jwt
from config import Config
from controllers.UserController import user_bp
from settings.aws_secret import awssecret, AwsSecretManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    swagger.init_app(app) 
    jwt.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(user_bp,url_prefix='/api/auth')
    app.register_blueprint(blueprint_home,url_prefix='/api/v1')
    
    awssecret = AwsSecretManager()
    secret = awssecret.get_secret('api_82')
    print(secret)

    @app.route('/')
    def home():
        return {'msj': 'hola mundoghghghghghg'}

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=  True, 
            host= '0.0.0.0')