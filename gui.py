# Verbindung zur Datenbank
# funktioniert noch nicht

import pymysql

def connect_to_database():
    try:
        connection = pymysql.connect(
            host="141.41.42.211",
            user="kompressor",
            password="InfoLabor_Gr2",
            database="kompressor",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        return connection
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
        return None


connect_to_database()