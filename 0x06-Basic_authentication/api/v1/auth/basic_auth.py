#!/usr/bin/env python3
""" Class Basic Auth """
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User
from models.base import DATA


class BasicAuth(Auth):
    """Basic Auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ extract header """
        if authorization_header is None:
            return None

        if type(authorization_header) is not str:
            return None

        if authorization_header.startswith("Basic "):
            return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ decode base64 header """
        if base64_authorization_header is None:
            return None

        if type(base64_authorization_header) is not str:
            return None

        try:
            return b64decode(base64_authorization_header,
                             None, True).decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ extract user credentials """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        return decoded_base64_authorization_header.split(":")

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """ extract object from credentials """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None

        if DATA.get("User") is None:
            return None

        users = User.search({"email": user_email})

        for user in users:
            if user_email == user.email and user.is_valid_password(user_pwd):
                return user
            elif user.email != user_email:
                return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user method """
        head = self.authorization_header(request)

        if not head:
            return None
        email, pwd = self.extract_user_credentials(
                                                   self.decode_base64_authorization_header(
                                                   self.extract_base64_authorization_header(
                                                   head)))

        return self.user_object_from_credentials(email, pwd)
