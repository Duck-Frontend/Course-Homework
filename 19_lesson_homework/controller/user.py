import hashlib

from db import Session
from model.user import User


class UserController:

    @staticmethod
    def register(name, email, password, password_repeat):
        if password != password_repeat:
            raise ValueError("Passwords do not match")

        with Session as session:
            existing_user = session.query(
                User).filter_by(email=User.email).first()
            if existing_user:
                raise ValueError("Username already taken")
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            new_user = User(name=name, password=hashed_password)

            session.add(new_user)

            session.commit()

            session.refresh(new_user)

        return "OK"

    @staticmethod
    def login(email, password):
        pass
