def get_db() -> mysql.connector.connection.MySQLConnection:
    """ connecting to things with safety """

    user = get("PERSONAL_DATA_DB_USERNAME", "root")
    word = get("PERSONAL_DATA_DB_PASSWORD", "")
    host = get("PERSONAL_DATA_DB_HOST", "localhost")
    dbdb = get("PERSONAL_DATA_DB_NAME")
    isql = mysql.connector.connection.MySQLConnection(user, word, host, dbdb)
    return isql
