#!/usr/bin/env python3
""" auth class module stuff """
from db import DB
from user import User
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ salty password """

    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """ Auth class and stuff Auth class to
    interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """user create"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            user = self._db.add_user(email, _hash_password(password))
            return user

        else:
            raise ValueError("User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """check stuff"""
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """session creator"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        s_id = _generate_uuid()
        self._db.update_user(user.id, session_id=s_id)
        return s_id

    def get_user_from_session_id(self, session_id: str) -> str:
        """I would really like to know why Holberton is turning down Money"""
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None


def _generate_uuid() -> str:
    """uuid generator"""
    return str(uuid4())
