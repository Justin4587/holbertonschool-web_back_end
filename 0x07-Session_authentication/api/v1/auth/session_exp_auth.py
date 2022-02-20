#!/usr/bin/env python3
""" Session exp auth class def """

from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """ session exp """

    def __init__(self):
        """ overload innit """
        if getenv("SESSION_DURATION"):
            self.session_duration = int(getenv("SESSION_DURATION"))
        else:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """creates something """
        sessId = super().create_session(user_id)
        if sessId is None:
            return None
        self.user_id_by_session_id[sessId] = {
            "user_id": user_id,
            "created_at": datetime.now()}
        return sessId

    def user_id_for_session_id(self, session_id=None):
        """ id for id """
        if session_id is None:
            return None
        sess_dict = self.user_id_by_session_id.get(session_id)
        if sess_dict is None:
            return None
        if self.session_duration <= 0:
            return sess_dict.get("user_id")
        if "created_at" not in sess_dict:
            return None
        sess_time = sess_dict.get("created_at") +\
         timedelta(seconds=self.session_duration)
        if sess_time < datetime.now():
            return None
        return sess_dict.get("user_id")
