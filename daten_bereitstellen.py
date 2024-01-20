import pymysql


# Verbindung zur Datenbank herstellen
def connect_to_database():
    try:
        connection = pymysql.connect(
            host="141.41.42.211",
            user="Kompressor",
            password="Kompressor12345%",
            database="kompressor",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        return connection
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
        return None


# Funktion, um die letzten Datensätze aus der Datenbank in eine daten_geraet zu speichern
def get_last_records(geraet):
    connection = connect_to_database()
    data_list = []

    if connection:
        try:
            with connection.cursor() as cursor:
                sql = f"SELECT * FROM {geraet} ORDER BY zeitstempel"
                cursor.execute(sql)
                records = cursor.fetchall()
                data_list = [record for record in records]

        except (
            pymysql.Error
        ) as e:  # Diese Zeile könnte möglicherweise falsch eingerückt sein
            print(f"Error fetching data from the database: {e}")

        finally:
            connection.close()

    return data_list


# Beispielaufruf, um die letzten Datensätze aus 'geraet' Tabelle in einer Liste zu speichern
last_records = get_last_records("geraet")

# Jetzt enthält 'last_records' eine Liste von Dictionaries mit den letzten Datensätzen

# Die letzten 20 Datensätze ausgeben und Zeitstempel ändern
for record in last_records:
    # Ändern des Zeitstempelformats, falls 'zeitstempel' bereits ein datetime-Objekt ist
    formatted_timestamp = record["zeitstempel"].strftime("%d.%m.%Y %H:%M:%S")
    record[
        "zeitstempel"
    ] = formatted_timestamp  # Aktualisieren des Zeitstempels im Dictionary

# Beispielaufruf, um die letzten Datensätze aus 'geraet' Tabelle in einer Liste zu speichern
last_records = get_last_records("geraet")

# Überprüfe, ob 'daten_geraet' bereits vorhanden ist
if "daten_geraet" not in locals():
    # Wenn 'daten_geraet' noch nicht vorhanden ist, initialisiere eine neue leere Liste
    daten_geraet = []

for record in last_records:
    # Ändern des Zeitstempelformats, falls 'zeitstempel' bereits ein datetime-Objekt ist
    formatted_timestamp = record["zeitstempel"].strftime("%Y-%m-%d %H:%M:%S")
    record[
        "zeitstempel"
    ] = formatted_timestamp  # Aktualisieren des Zeitstempels im Dictionary

    # Direkt den Datensatz zur vorhandenen Liste 'daten_geraet' hinzufügen
    daten_geraet.append(record)


# Funktion, um die letzten Datensätze aus der Datenbank in eine daten_sensor zu speichern
def get_last_records(sensor):
    connection = connect_to_database()
    data_list = []

    if connection:
        try:
            with connection.cursor() as cursor:
                sql = f"SELECT * FROM {sensor} ORDER BY zeitstempel"  # Annahme: 'id' ist die Primärschlüsselspalte
                cursor.execute(sql)
                records = cursor.fetchall()
                data_list = [record for record in records]

        except (
            pymysql.Error
        ) as e:  # Diese Zeile könnte möglicherweise falsch eingerückt sein
            print(f"Error fetching data from the database: {e}")

        finally:
            connection.close()

    return data_list


# Beispielaufruf, um die letzten Datensätze aus 'sensor' Tabelle in einer Liste zu speichern
last_records = get_last_records("sensor")

# Jetzt enthält 'last_records' eine Liste von Dictionaries mit den letzten Datensätzen

# Die letzten 20 Datensätze ausgeben und Zeitstempel ändern
for record in last_records:
    # Ändern des Zeitstempelformats, falls 'zeitstempel' bereits ein datetime-Objekt ist
    formatted_timestamp = record["zeitstempel"].strftime("%d.%m.%Y %H:%M:%S")
    record[
        "zeitstempel"
    ] = formatted_timestamp  # Aktualisieren des Zeitstempels im Dictionary

# Beispielaufruf, um die letzten Datensätze aus 'geraet' Tabelle in einer Liste zu speichern
last_records = get_last_records("sensor")

# Überprüfe, ob 'daten_sensor' bereits vorhanden ist
if "daten_sensor" not in locals():
    # Wenn 'daten_geraet' noch nicht vorhanden ist, initialisiere eine neue leere Liste
    daten_sensor = []

for record in last_records:
    # Ändern des Zeitstempelformats, falls 'zeitstempel' bereits ein datetime-Objekt ist
    formatted_timestamp = record["zeitstempel"].strftime("%Y-%m-%d %H:%M:%S")
    record[
        "zeitstempel"
    ] = formatted_timestamp  # Aktualisieren des Zeitstempels im Dictionary

    # Direkt den Datensatz zur vorhandenen Liste 'daten_sensor' hinzufügen (hier fügst du den gesamten Datensatz hinzu)
    daten_sensor.append(record)


def merge_data(daten_geraet, daten_sensor):
    daten_komplett = []

    sensor_dict = {}
    for sensor_datensatz in daten_sensor:
        if sensor_datensatz["datas_id"] is not None:
            key = (sensor_datensatz["datas_id"], sensor_datensatz["zeitstempel"])
            sensor_dict[key] = sensor_datensatz

    for geraet_datensatz in daten_geraet:
        if (
            geraet_datensatz["geraet_id"] == 1
            and geraet_datensatz["datas_id"] is not None
        ):
            key = (geraet_datensatz["datas_id"], geraet_datensatz["zeitstempel"])
            if key in sensor_dict:
                sensor_datensatz = sensor_dict[key]
                geraet_datensatz["druck"] = sensor_datensatz["druck"]
                geraet_datensatz["durchfluss"] = sensor_datensatz["durchfluss"]
                geraet_datensatz["temperatur"] = sensor_datensatz["temperatur"]
            else:
                # Setze die Werte auf None, wenn kein passender Datensatz gefunden wird
                geraet_datensatz["druck"] = None
                geraet_datensatz["durchfluss"] = None
                geraet_datensatz["temperatur"] = None
        else:
            # Für Datensätze, die nicht geraet_id 1 entsprechen, oder keine datas_id haben
            geraet_datensatz["druck"] = None
            geraet_datensatz["durchfluss"] = None
            geraet_datensatz["temperatur"] = None

        daten_komplett.append(geraet_datensatz)

    return daten_komplett


daten_komplett = merge_data(daten_geraet, daten_sensor)
print(daten_komplett)


def bearbeite_datensaetze(daten_geraet):
    # Schritt 1: Zeilen löschen, wo geraet_id gleich 4 ist

    gesamt_energie_daten = {}
    for datensatz in daten_geraet:
        if datensatz["geraet_id"] != 4:
            zeitstempel = datensatz["zeitstempel"]
            energie = datensatz["energie"]
            if zeitstempel in gesamt_energie_daten:
                gesamt_energie_daten[zeitstempel] += energie
            else:
                gesamt_energie_daten[zeitstempel] = energie

    # Den neuen Datensatz "gesamt_energie_daten" erstellen
    gesamt_energie_datensaetze = []
    for zeitstempel, energie in gesamt_energie_daten.items():
        datensatz = {
            "geraet_id": 0,
            "zeitstempel": zeitstempel,
            "gesamt_energie": energie,
        }
        gesamt_energie_datensaetze.append(datensatz)

    return gesamt_energie_datensaetze


gesamt_daten = bearbeite_datensaetze(daten_geraet)
print(gesamt_daten)
