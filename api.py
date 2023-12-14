import requests
import pymysql

comp_url = "http://141.41.235.28/JSON_Kompressor_IPT/Kompressor_Json.php"
response = requests.get(comp_url)
data = response.json()

relevant_keys = {
    "Kompressor_IPT": ["ID", "Zeitstempel", "Energie_gesamt_kwh"], #GeräteID 1
    "Kompressor_IPT_Entlueftung": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],  #GeräteID 2
    "Kompressor_IPT_Kuehler": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],  #GeräteID 3
    "Kompressor_IPT_Sensoren": ["ID", "Zeitstempel", "Druck", "Durchfluss", "Temperatur1"], #SensorID 1
    "Kompressor_Ostfalia": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],  #GeräteID 4
} #Geräte ID 0 ist für das Testing
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

def connect_to_database():
    try:
        connection = pymysql.connect(host='141.41.42.211',
                                 user='Kompressor',
                                 password='Kompressor12345%',
                                 database='kompressor',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        return connection
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def insert_test_data():
    connection = connect_to_database()
    try:
        with connection.cursor() as cursor:
            # Beispiel-Datensatz zum Einfügen
            test_data = {
                "ID_Geraet": 0,
                "Bereich": "Test",
                "Zeitstempel": "2023-01-01 12:00:00",
                "Energie": 1000,
                "Sensor": 0,
            }

            # SQL-Anweisung zum Einfügen der Daten
            sql = "INSERT INTO geraet (gerät_id, bereich, zeitstempel, energie, sensor_id) VALUES (%s, %s, %s, %s, %s)"

            cursor.execute(sql, (test_data["ID_Geraet"], test_data["Bereich"], test_data["Zeitstempel"], test_data["Energie"], test_data["Sensor"]))

        connection.commit()
    except pymysql.Error as e:
        print(f"Error inserting data into the database: {e}")
    finally:
        # Schließe die Verbindung
        connection.close()
def delete_test_data():
    connection = connect_to_database()

    if connection:
        try:
            with connection.cursor() as cursor:
                # SQL-Anweisung zum Löschen des Testdatensatzes
                sql = "DELETE FROM geraet WHERE gerät_id = %s"

                # Führe die SQL-Anweisung aus
                cursor.execute(sql, 0)

            # Commit, um die Änderungen in der Datenbank zu speichern
            connection.commit()

        except pymysql.Error as e:
            print(f"Error deleting data from the database: {e}")
        finally:
            # Schließe die Verbindung
            connection.close()

def insert_data(relevant_data):
    connection = connect_to_database()

    if connection:
        try:
            with connection.cursor() as cursor:
                for category, entries in relevant_data.items():
                    for entry in entries:
                        # Überprüfe, ob es sich um Sensoren handelt
                        if category == "Kompressor_IPT_Sensoren":
                            # SQL-Anweisung zum Einfügen der Sensordaten
                            sql = "INSERT INTO sensor (datas_id, zeitstempel, druck, durchfluss, temperatur, sensor_id) VALUES (%s, %s, %s, %s, %s, %s)"

                            # Führe die SQL-Anweisung mit den Sensordaten aus
                            cursor.execute(sql, (
                                entry["ID"],
                                entry["Zeitstempel"],
                                entry["Druck"],
                                entry["Durchfluss"],
                                entry["Temperatur1"],
                                1 # nur ein Sensor
                            ))
                        elif category == "Kompressor_IPT":

                            # Für alle anderen Kategorien (Geräte)
                            # SQL-Anweisung zum Einfügen der Gerätedaten
                            sql = "INSERT INTO geraet (datag_id, bereich, zeitstempel, energie, geraet_id, datas_id) VALUES (%s, %s, %s, %s, %s, %s)"

                            # Führe die SQL-Anweisung mit den Gerätedaten aus
                            cursor.execute(sql, (
                                entry["ID"],
                                category,
                                entry["Zeitstempel"],
                                entry["Energie_gesamt_kwh"],
                                get_geraete_id(category),
                                relevant_data["Kompressor_IPT_Sensoren"][0]["ID"]
                            ))
                        else:
                            sql = "INSERT INTO geraet (datag_id, bereich, zeitstempel, energie, geraet_id) VALUES (%s, %s, %s, %s, %s)"

                            # Führe die SQL-Anweisung mit den Gerätedaten aus
                            cursor.execute(sql, (
                                entry["ID"],
                                category,
                                entry["Zeitstempel"],
                                entry["Energie_gesamt_kwh"],
                                get_geraete_id(category)
                            ))

            # Commit, um die Änderungen in der Datenbank zu speichern
            connection.commit()

        except pymysql.Error as e:
            print(f"Error inserting data into the database: {e}")
        finally:
            # Schließe die Verbindung
            connection.close()

def get_geraete_id(category):
    if category == "Kompressor_IPT":
        return 1
    elif category == "Kompressor_IPT_Entlueftung":
        return 2
    elif category == "Kompressor_IPT_Kuehler":
        return 3
    elif category == "Kompressor_Ostfalia":
        return 4
    else:
        return None


if __name__ == '__main__':
    relevant_data = get_relevant_data(data, relevant_keys)
    # Füge die relevanten Daten in die Datenbank ein
    insert_data(relevant_data)

