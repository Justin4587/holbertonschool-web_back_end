#!/usr/bin/env python3
""" I will do my own filtering thank you. """

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, seperator: str) -> str:
    """ I believe I should be removing things """

    for _ in fields:
        youveGotMail = re.sub(_ + ".*?" + seperator,
                              _ + "=" + redaction + seperator, message)

    return youveGotMail
