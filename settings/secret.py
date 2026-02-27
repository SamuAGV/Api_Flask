# settings/secret.py
import os
import json
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class SecretManager:
    """
    Clase para manejar secrets de la aplicación
    get_sm: Obtener secretos
    set_sm: Establecer secretos (para este caso, desde variables de entorno)
    """
    
    _instance = None
    _secrets = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_secrets()
        return cls._instance
    
    def _load_secrets(self):
        """Cargar todos los secrets desde variables de entorno"""
        self._secrets = {
            'FLASK_ENV': os.getenv('FLASK_ENV', 'development'),
            'DATABASE_URI': os.getenv('DATABASE_URI', ''),
            'SECRET_KEY': os.getenv('SECRET_KEY', ''),
            'JWT_SECRET_KEY': os.getenv('JWT_SECRET_KEY', ''),
            # Puedes agregar más secrets aquí
        }
    
    def get_sm(self, key, default=None):
        """
        Obtener un secret por su clave
        Uso: secret_manager.get_sm('DATABASE_URI')
        """
        return self._secrets.get(key, default)
    
    def set_sm(self, key, value):
        """
        Establecer un secret en tiempo de ejecución
        Uso: secret_manager.set_sm('DATABASE_URI', 'mysql://...')
        """
        self._secrets[key] = value
        # Opcional: también establecer en variable de entorno
        os.environ[key] = str(value)
        return True
    
    def get_all_secrets(self):
        """Obtener todos los secrets (útil para debugging)"""
        # Ocultar valores sensibles parcialmente
        safe_secrets = {}
        for key, value in self._secrets.items():
            if any(sensitive in key.upper() for sensitive in ['KEY', 'SECRET', 'PASSWORD']):
                safe_secrets[key] = value[:4] + '****' if value and len(value) > 4 else '****'
            else:
                safe_secrets[key] = value
        return safe_secrets
    
    def reload_from_env(self):
        """Recargar secrets desde variables de entorno"""
        self._load_secrets()
        return True


# Crear instancia única (singleton)
secret_manager = SecretManager()

# Funciones de conveniencia para acceso directo
def get_sm(key, default=None):
    """Función helper para obtener secrets"""
    return secret_manager.get_sm(key, default)

def set_sm(key, value):
    """Función helper para establecer secrets"""
    return secret_manager.set_sm(key, value)