from api import *

def test_api_request_successful():
    assert response.status_code == 200

def test_api_request_returns_json():
    assert response.headers['Content-Type'] == 'application/json'


def test_get_relevant_data():

    result = get_relevant_data(data, relevant_keys)

    # Überprüfe, ob das Ergebnis ein Dictionary ist
    assert isinstance(result, dict)

    # Überprüfe, ob jede Kategorie im Ergebnis ein Dictionary mit einer Liste von Dictionaries ist
    for category, data_list in result.items():
        assert isinstance(data_list, list)
        assert all(isinstance(entry, dict) for entry in data_list)

        # Überprüfe, ob alle erwarteten Schlüssel in jedem Dictionary vorhanden sind
        for entry in data_list:
            assert all(key in entry for key in relevant_keys[category])

def test_connect_to_database():
    # Call the function to connect to the database
    connection = connect_to_database()

    # Assert that the connection is not None
    assert connection is not None

    # Assert that the connection is of the correct type
    assert isinstance(connection, pymysql.connections.Connection)

def test_insert_data_into_database():
    # Füge Testdaten zur Datenbank hinzu
    insert_test_data()

    # Verbinde erneut zur Datenbank, um die eingefügten Daten abzufragen
    connection = connect_to_database()

    if connection:
        try:
            with connection.cursor() as cursor:
                # SQL-Anweisung zum Abfragen des eingefügten Datensatzes
                sql = "SELECT * FROM gerät WHERE gerät_id = %s"

                # Führe die SQL-Anweisung aus
                cursor.execute(sql, 0)

                # Überprüfe, ob der Datensatz vorhanden ist
                result = cursor.fetchone()
                assert result is not None

        finally:
            delete_test_data()
            # Schließe die Verbindung
            connection.close()

