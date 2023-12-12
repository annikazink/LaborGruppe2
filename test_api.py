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

def test_turn_data_into_list(): #turn data into list for database
    pass

def test_connect_to_database():
    pass

def test_insert_data_into_database():
    pass

def test_close_database_connection():
    pass




