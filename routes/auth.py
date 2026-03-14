from flask import Blueprint, request, jsonfy
from auth.cognito_service import create_cognito_user
from models.user import User
from extensions import db

auth_bpc = Blueprint ("cognito_auth",__name__)


@auth_bpc.routes("/register", methods=["POST"])
def register():
    """"
    Registrar usuario en Cognito
    """
    tags:
        - Cognito
    consumes:
        -application/json
    paramaters:
    - in: body
    name: body
    required: True
    schema: