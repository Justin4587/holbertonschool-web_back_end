#!/usr/bin/env python3
""" session db auth class """
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """" same damn thing """

    def create_session(self, user_id=None):
        """ create session """

        sess_id = super().create_session(user_id)
        new_sess = UserSession()
        new_sess.user_id = user_id
        new_sess.session_id = sess_id
        new_sess.save()

        return sess_id

    def user_id_for_session_id(self, session_id=None):
        """ same time trade """
        user_id = super().user_id_for_session_id(session_id)
        return user_id

    def destroy_session(self, user_id=None):
        """ destroy it if it matches"""
        cook = self.session_cookie(request)
        if request is None or cook is None:
            return False
        all_sess = UserSession.all()
        for session in all_sess:
            if session.session_id == cook:
                del session
        return True
