#!/usr/bin/env python3
""" I will do my own filtering thank you. """

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ I believe I should be removing things """

    for _ in fields:
        youveGotMail = re.sub(_ + ".*?" + separator,
                              _ + "=" + redaction + separator, message)

    return youveGotMail
