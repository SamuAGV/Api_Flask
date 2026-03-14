# auth.py
from flask import Blueprint, request, jsonify
from auth.cognito_service import create_cognito_user
from models.user import User
from extensions import db

auth_bpc = Blueprint("cognito_auth", __name__)

@auth_bpc.route("/register", methods=["POST"])
def register():
    """
    Registrar usuario en Cognito
    ---
    tags:
      - Cognito
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
            password:
              type: string
            mobe:
              type: string
    responses:
      201:
        description: Usuario creado correctamente
      400:
        description: Datos incompletos
      500:
        description: Error interno del servidor
    """
    try:
        # Obtener datos de la solicitud
        data = request.json
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400
            
        email = data.get("email")
        password = data.get("password")
        mobe = data.get("mobe")  # Campo opcional

        # Validar campos requeridos
        if not email or not password:
            return jsonify({"error": "Datos incompletos. Email y password son requeridos"}), 400

        # Crear usuario en Cognito
        try:
            sub = create_cognito_user(email, password)
        except Exception as e:
            return jsonify({"error": f"Error al crear usuario en Cognito: {str(e)}"}), 500

        # Crear usuario en base de datos local
        try:
            user = User(
                email=email,
                cognito_sub=sub,  # Asumo que este campo existe en tu modelo
                mobe=mobe
            )
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            # Si falla la BD, deberíamos considerar eliminar el usuario de Cognito
            # o al menos registrar el error para consistencia
            return jsonify({"error": f"Error al guardar usuario en BD: {str(e)}"}), 500

        # Respuesta exitosa
        return jsonify({
            "message": "Usuario creado correctamente",
            "user": {
                "email": email,
                "sub": sub
            }
        }), 201

    except Exception as e:
        # Error general no controlado
        return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500