#!/usr/bin/env python3
""" Class Basic Auth """
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth"""
    
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ extract header """
        if authorization_header is None or type(authorization_header) is not str:
            return None

        if authorization_header.startswith("Basic "):
            return authorization_header[6:]
