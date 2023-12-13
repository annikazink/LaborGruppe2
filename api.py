import requests
import pymysql

comp_url = "http://141.41.235.28/JSON_Kompressor_IPT/Kompressor_Json.php"
response = requests.get(comp_url)
data = response.json()

relevant_keys = {
    "Kompressor_IPT": ["ID", "Zeitstempel", "Strom_gesamt"],
    "Kompressor_IPT_Entlueftung": ["ID", "Zeitstempel", "Strom_gesamt"],
}
def get_relevant_data(api_response, relevant_keys):
    relevant_data = {}

    for category, keys in relevant_keys.items():
        if category in api_response:
            relevant_data[category] = []

            for entry in api_response[category]:
                relevant_entry = {}
                for key in keys:
                    relevant_entry[key] = entry.get(key)

                relevant_data[category].append(relevant_entry)

    return relevant_data

def convert_strings_to_float(data):
    for category, entries in data.items():
        for entry in entries:
            for key, value in entry.items():
                if isinstance(value, str):
                    try:
                        entry[key] = float(value)
                    except ValueError:
                        pass




def connect_to_database():
    try:
        connection = pymysql.connect(host='127.0.0.1',
                                 user='kompressor',
                                 password='InfoLabor_Gr2',
                                 database='kompressor',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        return connection
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def insert_data_into_database():
    pass

def close_database_connection():
    pass


def insert_test_data():
    connection = connect_to_database()


    try:
        with connection.cursor() as cursor:
            # Beispiel-Datensatz zum Einfügen
            test_data = {
                "ID": 123,
                "Zeitstempel": "2023-12-14 12:00:00",
                "Strom_gesamt": 10.5
                # Füge hier weitere Felder und Werte hinzu
            }

            # SQL-Anweisung zum Einfügen der Daten
            sql = "INSERT INTO gerät (bereich, zeitstempel, energie) VALUES (%s, %s, %s)"

            # Führe die SQL-Anweisung mit den Testdaten aus
            cursor.execute(sql, (test_data["ID"], test_data["Zeitstempel"], test_data["Strom_gesamt"]))

        # Commit, um die Änderungen in der Datenbank zu speichern
        connection.commit()
    except pymysql.Error as e:
        print(f"Error inserting data into the database: {e}")
    finally:
        # Schließe die Verbindung
        connection.close()


if __name__ == '__main__':
    # Füge Testdaten zur Datenbank hinzu
    insert_test_data()

