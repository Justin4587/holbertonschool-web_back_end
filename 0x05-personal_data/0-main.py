#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;date_of_birth=12/12/1986;password=eggcellent;", "name=bob;email=bob@dylan.com;date_of_birth=03/04/1993;password=bobbycool;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
