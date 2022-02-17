#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ method to enforce authentication """
        if path is None:
            return True

        if path[-1] != '/':
            path += '/'

        return False

    def authorization_header(self, request=None) -> str:
        """words that will equal points"""
        if request is None:
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar("User"):
        """ returns none """
        return None
