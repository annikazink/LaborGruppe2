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

def test_convert_strings_to_float():
    # Testfall 1: Float-Wert wird korrekt konvertiert
    data = {"category": [{"key": "ID", "value": "42.0"}]}
    convert_strings_to_float(data)
    assert data == {"category": [{"key": "ID", "value": 42.0}]}

    # Testfall 2: Nicht konvertierbarer String bleibt unverändert
    data = {"category": [{"key": "ID", "value": "abc"}]}
    convert_strings_to_float(data)
    assert data == {"category": [{"key": "ID", "value": "abc"}]}

    # Testfall 3: Keine Konvertierung für Nicht-String-Werte
    data = {"category": [{"key": "ID", "value": 42.0}]}
    convert_strings_to_float(data)
    assert data == {"category": [{"key": "ID", "value": 42.0}]}

def test_turn_data_into_list(): #turn data into list for database
    pass

def test_extract_values_into_flat_list():
    relevant_data = {
        'Kompressor_IPT': [{'ID': '12252969', 'Zeitstempel': '2023-12-13 15:32:08.056', 'Strom_gesamt': '0.029967365722287524'}],
        'Kompressor_IPT_Entlueftung': [{'ID': '12250918', 'Zeitstempel': '2023-12-13 15:32:08.036', 'Strom_gesamt': '0.013315'}]
    }

    result = extract_values_into_flat_list(relevant_data)

    # Überprüfe, ob das Ergebnis eine Liste ist
    assert isinstance(result, list)

    # Überprüfe, ob die Werte korrekt extrahiert wurden
    assert result == ['12252969', '2023-12-13 15:32:08.056', '0.029967365722287524', '12250918', '2023-12-13 15:32:08.036', '0.013315']


def test_connect_to_database():
    # Call the function to connect to the database
    connection = connect_to_database()

    # Assert that the connection is not None
    assert connection is not None

    # Assert that the connection is of the correct type
    assert isinstance(connection, pymysql.connections.Connection)

def test_insert_data_into_database():
    pass

def test_close_database_connection():
    pass




