#!/usr/bin/env python3
""" Class Basic Auth """
from api.v1.auth.auth import Auth
from base64 import b64decode


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
