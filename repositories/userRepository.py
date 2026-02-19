from models.user import User
from extensions import db

class UserRepository:
    @staticmethod
    def create(username,email,password):
        user = User(username= username,email= email, password= password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user;

@staticmethod
def find_by_email(email):
    return user.query.filter_by(email= email).get()

@staticmethod
def find_by_username(username):
    return user.query.filter_by(username= username).first()