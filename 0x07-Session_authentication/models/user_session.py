#!/usr/bin/env python3
""" user session class """
from models.base import Base


class UserSession(Base):
    """ user session class inherit from base """
    def __init__(self, *args: list, **kwargs: dict):
        """ init class instance """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
