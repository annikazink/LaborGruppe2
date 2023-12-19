"""

from api import *
from unittest.mock import patch, MagicMock

# Fügen Sie hier Importe für Ihre Testdaten hinzu, wenn sie externe Daten verwenden

@patch('api.requests.get')  # Mockt die 'requests.get'-Funktion, die für die API-Anfragen verwendet wird
def test_api_request_successful(mock_get):
    # Mock the response status code
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    # Test the function
    assert mock_response.status_code == 200

@patch('api.requests.get')
def test_api_request_returns_json(mock_get):
    # Mocken Sie die response-Variable
    mock_response = MagicMock()
    mock_response.headers = {'Content-Type': 'application/json'}
    mock_get.return_value = mock_response

    # Testen Sie die Funktion
    assert api_request_returns_json()

@patch('api.get_relevant_data')
def test_get_relevant_data(mock_get_relevant_data):
    # Mocken Sie die data-Variable und die relevant_keys-Variable
    mock_data = {}  # Fügen Sie hier Ihre Testdaten hinzu
    mock_relevant_keys = {}  # Fügen Sie hier Ihre Testdaten hinzu
    mock_get_relevant_data.return_value = mock_data

    # Testen Sie die Funktion
    result = get_relevant_data(mock_data, mock_relevant_keys)

    # Führen Sie Ihre vorhandenen Tests auf das Ergebnis durch

@patch('api.connect_to_database')
def test_connect_to_database(mock_connect_to_database):
    # Mocken Sie die Verbindung zur Datenbank
    mock_connection = MagicMock()
    mock_connect_to_database.return_value = mock_connection

    # Testen Sie die Funktion
    connection = connect_to_database()

    # Führen Sie Ihre vorhandenen Tests auf die 'connection'-Variable durch

@patch('api.connect_to_database')
@patch('api.insert_test_data')
@patch('api.delete_test_data')
def test_insert_data_into_database(mock_connect_to_database, mock_insert_test_data, mock_delete_test_data):
    # Mocken Sie die Verbindung zur Datenbank
    mock_connection = MagicMock()
    mock_connect_to_database.return_value = mock_connection

    # Testen Sie die Funktion
    insert_data_into_database()

    # Führen Sie Ihre vorhandenen Tests durch, die auf die Datenbank zugreifen


"""



"""
Hinweise
Eine Kopfzeile gehört überall hin / Es fehlen auch Kommentare

die Tests sehen schon ok aus, nur fehlen halt die Mock-Tests. Auch bauen die Test teilweise auf externen Daten auf
(response/data). Diese sollen in der Testumgebung definiert werden . Die Tests sollten isoliert voneinander laufen.

Es fehlen Tests, was passiert wenn die API einen Fehlercode zurückgibt

Wenn Sie die Mock Objekte hinzugefügt haben, sind diese Tests auch CI fähig, dh sie müssen
Attribute mit übertragen, "@pytest.mark.mockable" wenn Sie dann in github action datei pytest so:
      run: |
        pytest -m mockable
ausführen werden nur tests mit diesem Attribute in github actions durchlaufen und die tests sind dann positiv (die direkten Daten-
bankzugriffe könne sie virtuell ja nicht testen.

"""

"""
from api import *
import unittest
from unittest.mock import Mock, patch
import json
import responses

class TestApi(unittest.TestCase):
    def create_mock_response(self, status_code, data=None):
        mock_response = Mock()
        mock_response.status_code = status_code
        mock_response.json.return_value = data  # Verwenden Sie json-Methode, um die Daten abzurufen
        return mock_response

    @patch('api.requests.get')
    def test_api_request_successful(self, mock_get):
        expected_data = {"Kompressor_IPT": [...]}

        mock_response = self.create_mock_response(200, expected_data)
        mock_get.return_value = mock_response

        response = requests.get("http://141.41.235.28/JSON_Kompressor_IPT/Kompressor_Json.php")

        self.assertIsNotNone(response)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(), expected_data)



    @responses.activate
    def test_api_request_returns_json(self):
        url = "http://example.com/api"
        responses.add(responses.GET, url, json={"some_key": "some_value"}, status=200,
                      content_type='application/json')

        response = requests.get(url)
        assert response.headers['Content-Type'] == 'application/json'

    def test_get_relevant_data(self):
        # Erstellen Sie Mock-Daten für die API-Antwort
        mock_data = {
            "Kompressor_IPT": [{"ID": 1, "Zeitstempel": "2023-01-01", "Energie_gesamt_kwh": 100}],
            "Kompressor_IPT_Entlueftung": [{"ID": 2, "Zeitstempel": "2023-01-01", "Energie_gesamt_kwh": 200}],
        }

        result = Api.get_relevant_data(mock_data, Api.relevant_keys)

        # Überprüfen Sie, ob das Ergebnis ein Dictionary ist
        assert isinstance(result, dict)

        # Überprüfen Sie, ob jede Kategorie im Ergebnis ein Dictionary mit einer Liste von Dictionaries ist
        for category, data_list in result.items():
            assert isinstance(data_list, list)
            assert all(isinstance(entry, dict) for entry in data_list)

            # Überprüfen Sie, ob alle erwarteten Schlüssel in jedem Dictionary vorhanden sind
            for entry in data_list:
                assert all(key in entry for key in Api.relevant_keys[category])

    def test_connect_to_database(self):
        # Erstellen Sie einen Mock für die Datenbankverbindung
        with unittest.mock.patch("pymysql.connect") as mock_connect:
            # Setzen Sie die return_value des Mocks auf eine Instanz von pymysql.connections.Connection
            mock_connection = pymysql.connections.Connection()
            mock_connect.return_value = mock_connection

            # Rufen Sie die Funktion zum Verbinden mit der Datenbank auf
            connection = Api.connect_to_database()

            # Überprüfen Sie, ob die Verbindung nicht None ist
            assert connection is not None

            # Überprüfen Sie, ob die Verbindung vom richtigen Typ ist
            assert isinstance(connection, pymysql.connections.Connection)

    def test_insert_data_into_database(self):
        # Erstellen Sie Mock-Daten für die Datenbank
        mock_relevant_data = {
            "Kompressor_IPT": [{"ID": 1, "Zeitstempel": "2023-01-01", "Energie_gesamt_kwh": 100}],
            "Kompressor_IPT_Entlueftung": [{"ID": 2, "Zeitstempel": "2023-01-01", "Energie_gesamt_kwh": 200}],
        }

        # Rufen Sie die Funktion zum Einfügen der Daten in die Datenbank auf
        Api.insert_data(mock_relevant_data)

        # Überprüfen Sie, ob die Daten in der Datenbank vorhanden sind
        connection = Api.connect_to_database()

        if connection:
            try:
                with connection.cursor() as cursor:
                    # SQL-Anweisung zum Abfragen der eingefügten Datensätze
                    sql = "SELECT * FROM geraet"

                    # Führe die SQL-Anweisung aus
                    cursor.execute(sql)

                    # Überprüfen Sie, ob die Datensätze vorhanden sind
                    result = cursor.fetchall()
                    assert result is not None

            finally:
                # Schließe die Verbindung
                connection.close()
"""

from api import *
from unittest.mock import MagicMock, patch

class TestApi():
    def test_api_call_successfull(self):
        pass

    def test_api_call_unsuccessfull(self):
        pass

    def test_api_call_returns_json(self):
        pass

    def test_api_call_returns_no_json(self):
        pass
    def test_get_relevant_data(self):
        pass

    def test_did_not_get_relevant_data(self):
        pass

    def test_connection_to_database_successfull(self):
        pass

    def test_connection_to_database_unsuccessfull(self):
        pass
