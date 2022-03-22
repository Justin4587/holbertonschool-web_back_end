#!/usr/bin/env python3
"""list all or empty"""
from pymongo import MongoClient

def log_stats():
    """ the stuff"""
    Meth = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    client_logs = MongoClient().logs.nginx
    total_logs = client_logs.count_documents({})

    print(f"{total_logs} logs")
    print(f"Methods:")

    for m in Meth:
        count = client_logs.count_documents({'method':m})
        print(f'\tmethod {m}: {count}')
    stat = client_logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{stat} status check")

if __name__ == "__main__":
    log_stats()
