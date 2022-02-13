#!/usr/bin/env python3
""" I will do my own filtering thank you. """

import re
from typing import List
import logging


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
        message = re.sub(f"{target}=.*?{separator}",
                         f"{target}={redaction}{separator}", message)

    return message
