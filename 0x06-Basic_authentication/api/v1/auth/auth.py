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
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if path[-1] != '/':
            path += '/'

        if excluded_paths[-1] != '/':
            excluded_paths += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """words that will equal points"""
        if request is None or request.headers.get("Authorization") is None:
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar("User"):
        """ returns none """
        return None
