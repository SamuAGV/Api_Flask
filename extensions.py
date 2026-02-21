from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()

swagger = Swagger(template={
    "swagger":"2.0",
    "info": {
        "title": "api 82"
        },
        "securityDefinitions":{
        "Bearertokenth":{
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Coloca Bearer <tu-token>"
        }
    }
})

jwt = JWTManager()   