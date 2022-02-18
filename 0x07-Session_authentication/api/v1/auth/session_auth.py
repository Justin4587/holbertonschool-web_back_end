#!/usr/bin/env python3
""" session Authorization """
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """empty class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates session """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ user id method """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ current user """
        session = self.session_cookie(request)
        if session is None:
            return None
        user = self.user_id_for_session_id(session)

        return User.get(user)
