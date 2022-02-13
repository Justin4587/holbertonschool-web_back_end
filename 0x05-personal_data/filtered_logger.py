#!/usr/bin/env python3
""" I will do my own filtering thank you. """

import re
from typing import List
import logging
from os import environ
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class needs more words """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Redacting Formatter class needs more words """

        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Redacting Formatter class needs more words """

        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ I believe I should be removing things """

    for target in fields:
        hvt = '{target}=(.*?){separator}'
        placebo = '{target}={redaction}{separator}'

        message = re.sub(hvt, placebo, message)

    return message


def get_logger() -> logging.Logger:
    """ I wonder if theres any logging inolved """

    turd = logging.getLogger('user_data')
    turd.setLevel(logging.INFO)
    turd.propagate = False
    handled = logging.StreamHandler()
    handled.setFormatter(RedactingFormatter(PII_FIELDS))
    turd.addHandler(handled)

    return turd


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ connecting to things with safety """

    user = get("PERSONAL_DATA_DB_USERNAME", "root")
    word = get("PERSONAL_DATA_DB_PASSWORD", "")
    host = get("PERSONAL_DATA_DB_HOST", "localhost")
    dbdb = get("PERSONAL_DATA_DB_NAME")
    isql = mysql.connector.connection.MySQLConnection(user, word, host, dbdb)

    return isql
