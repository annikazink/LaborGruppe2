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

    def test_api_call_unsuccessfull(self):
        mock_response = MagicMock()

        # Setzen Sie den gewünschten Statuscode
        mock_response.status_code = 404

        # Mocken Sie requests.get
        with patch("requests.get", return_value=mock_response):
            # Rufen Sie die Funktion auf, die requests.get verwendet
            api_instance = Api()
            result = api_instance.get_response_url("http://example.com")

        assert result == "URL nicht gefunden"

    @patch("api.requests.get")
    def test_get_response_url_successfull(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"Kompressor_IPT":[{"ID":"12205254","Zeitstempel":"2023-11-10 11:56:27.410","Zeitstempel_ms":"1699617387410","Zeitstempel_Unix_ms":"1699613787410","Strom_gesamt":"0.029684464090384603","Spannung_gesamt":"399.5476327691272","Wirkleistung_gesamt":"10.15","Scheinleistung_gesamt":"12.133571225999999","Blindleistung_gesamt":"6.648387074803566","Energie_gesamt_kwh":"18988.191285","cosPhi_gesamt":"0.3333333333333333","Phi_gesamt":"0.19329719425651024","sinPhi_gesamt":"0.18264441553577956","Frequenz_gesamt":"50","Strom_Phase1":"0","Spannung_Phase1":"229.8694","Wirkleistung_Phase1":"0","Scheinleistung_Phase1":"0","Blindleistung_Phase1":"0","Energie_Phase1_kwh":"6054.99972","cosPhi_Phase1":"0","Phi_Phase1":"0","sinPhi_Phase1":"0","Frequenz_Phase1":"50","Strom_Phase2":"0","Spannung_Phase2":"230.5886","Wirkleistung_Phase2":"0","Scheinleistung_Phase2":"0","Blindleistung_Phase2":"0","Energie_Phase2_kwh":"6387.277785","cosPhi_Phase2":"0","Phi_Phase2":"0","sinPhi_Phase2":"0","Frequenz_Phase2":"50","Strom_Phase3":"0.051414999999999995","Spannung_Phase3":"231.5788","Wirkleistung_Phase3":"10.15","Scheinleistung_Phase3":"12.133571225999999","Blindleistung_Phase3":"6.648387074803566","Energie_Phase3_kwh":"6545.91378","cosPhi_Phase3":"1","Phi_Phase3":"0.5798915827695307","sinPhi_Phase3":"0.5479332466073387","Frequenz_Phase3":"50"}],"Kompressor_IPT_Entlueftung":[{"ID":"12203203","Zeitstempel":"2023-11-1011:56:27.390","Zeitstempel_ms":"1699617387390","Zeitstempel_Unix_ms":"1699613787390","Strom_gesamt":"0.013505000000000001","Spannung_gesamt":"230.59040000000002","Wirkleistung_gesamt":"1.44","Scheinleistung_gesamt":"3.0380285200000006","Blindleistung_gesamt":"2.675073323917196","Energie_gesamt_kwh":"36.17966","cosPhi_gesamt":"0.75","Phi_gesamt":"1.076977868369864","sinPhi_gesamt":"0.8805293651151094","Frequenz_gesamt":"50"}],"Kompressor_IPT_Kuehler":[{"ID":"12203200","Zeitstempel":"2023-11-1011:56:27.400","Zeitstempel_ms":"1699617387400","Zeitstempel_Unix_ms":"1699613787400","Strom_gesamt":"1.75798","Spannung_gesamt":"229.9522","Wirkleistung_gesamt":"251.99","Scheinleistung_gesamt":"403.84320340100004","Blindleistung_gesamt":"315.57942396991206","Energie_gesamt_kwh":"1008.193971","cosPhi_gesamt":"0.623","Phi_gesamt":"0.8969710172255206","sinPhi_gesamt":"0.7814404732139428","Frequenz_gesamt":"50"}],"Kompressor_IPT_Sensoren":[{"ID":"4639874","Zeitstempel":"2023-11-1011:56:27.380","Zeitstempel_ms":"1699617387380","Zeitstempel_Unix_ms":"1699613787380","Druck":"7.04412","Durchfluss":"132.202","Temperatur1":"23.898","Temperatur2":"1372"}],"Kompressor_Ostfalia":[{"ID":"12205255","Zeitstempel":"2023-11-1011:56:27.310","Zeitstempel_ms":"1699617387310","Zeitstempel_Unix_ms":"1699613787310","Strom_gesamt":"0.06227877353748492","Spannung_gesamt":"399.2848229265921","Wirkleistung_gesamt":"13.650000000000002","Scheinleistung_gesamt":"25.107655195","Blindleistung_gesamt":"14.859715638930806","Energie_gesamt_kwh":"11108.303394999999","cosPhi_gesamt":"0.11099999999999999","Phi_gesamt":"0.6881213930770241","sinPhi_gesamt":"0.4912569731672557","Frequenz_gesamt":"50","Strom_Phase1":"0.08406999999999999","Spannung_Phase1":"230.20620000000002","Wirkleistung_Phase1":"17.150000000000002","Scheinleistung_Phase1":"19.474293489","Blindleistung_Phase1":"9.226353932930806","Energie_Phase1_kwh":"3909.048675","cosPhi_Phase1":"0.833","Phi_Phase1":"0.4935678524361759","sinPhi_Phase1":"0.47377091950176703","Frequenz_Phase1":"50","Strom_Phase2":"0","Spannung_Phase2":"230.45260000000002","Wirkleistung_Phase2":"0","Scheinleistung_Phase2":"0","Blindleistung_Phase2":"0","Energie_Phase2_kwh":"3635.096885","cosPhi_Phase2":"0","Phi_Phase2":"0","sinPhi_Phase2":"0","Frequenz_Phase2":"50","Strom_Phase3":"0.023799999999999998","Spannung_Phase3":"230.92280000000002","Wirkleistung_Phase3":"-3.5","Scheinleistung_Phase3":"5.6333617060000005","Blindleistung_Phase3":"5.6333617060000005","Energie_Phase3_kwh":"3564.157835","cosPhi_Phase3":"-0.5","Phi_Phase3":"1.5707963267948966","sinPhi_Phase3":"1","Frequenz_Phase3":"50"}]}
        mock_response.status_code = 200
        mock_requests_get.return_value = mock_response

        api_instance = Api()

        with patch("api.requests.get", mock_requests_get):
            result = api_instance.get_response_url("http://example.com")
            assert result == {"Kompressor_IPT":[{"ID":"12205254","Zeitstempel":"2023-11-10 11:56:27.410","Zeitstempel_ms":"1699617387410","Zeitstempel_Unix_ms":"1699613787410","Strom_gesamt":"0.029684464090384603","Spannung_gesamt":"399.5476327691272","Wirkleistung_gesamt":"10.15","Scheinleistung_gesamt":"12.133571225999999","Blindleistung_gesamt":"6.648387074803566","Energie_gesamt_kwh":"18988.191285","cosPhi_gesamt":"0.3333333333333333","Phi_gesamt":"0.19329719425651024","sinPhi_gesamt":"0.18264441553577956","Frequenz_gesamt":"50","Strom_Phase1":"0","Spannung_Phase1":"229.8694","Wirkleistung_Phase1":"0","Scheinleistung_Phase1":"0","Blindleistung_Phase1":"0","Energie_Phase1_kwh":"6054.99972","cosPhi_Phase1":"0","Phi_Phase1":"0","sinPhi_Phase1":"0","Frequenz_Phase1":"50","Strom_Phase2":"0","Spannung_Phase2":"230.5886","Wirkleistung_Phase2":"0","Scheinleistung_Phase2":"0","Blindleistung_Phase2":"0","Energie_Phase2_kwh":"6387.277785","cosPhi_Phase2":"0","Phi_Phase2":"0","sinPhi_Phase2":"0","Frequenz_Phase2":"50","Strom_Phase3":"0.051414999999999995","Spannung_Phase3":"231.5788","Wirkleistung_Phase3":"10.15","Scheinleistung_Phase3":"12.133571225999999","Blindleistung_Phase3":"6.648387074803566","Energie_Phase3_kwh":"6545.91378","cosPhi_Phase3":"1","Phi_Phase3":"0.5798915827695307","sinPhi_Phase3":"0.5479332466073387","Frequenz_Phase3":"50"}],"Kompressor_IPT_Entlueftung":[{"ID":"12203203","Zeitstempel":"2023-11-1011:56:27.390","Zeitstempel_ms":"1699617387390","Zeitstempel_Unix_ms":"1699613787390","Strom_gesamt":"0.013505000000000001","Spannung_gesamt":"230.59040000000002","Wirkleistung_gesamt":"1.44","Scheinleistung_gesamt":"3.0380285200000006","Blindleistung_gesamt":"2.675073323917196","Energie_gesamt_kwh":"36.17966","cosPhi_gesamt":"0.75","Phi_gesamt":"1.076977868369864","sinPhi_gesamt":"0.8805293651151094","Frequenz_gesamt":"50"}],"Kompressor_IPT_Kuehler":[{"ID":"12203200","Zeitstempel":"2023-11-1011:56:27.400","Zeitstempel_ms":"1699617387400","Zeitstempel_Unix_ms":"1699613787400","Strom_gesamt":"1.75798","Spannung_gesamt":"229.9522","Wirkleistung_gesamt":"251.99","Scheinleistung_gesamt":"403.84320340100004","Blindleistung_gesamt":"315.57942396991206","Energie_gesamt_kwh":"1008.193971","cosPhi_gesamt":"0.623","Phi_gesamt":"0.8969710172255206","sinPhi_gesamt":"0.7814404732139428","Frequenz_gesamt":"50"}],"Kompressor_IPT_Sensoren":[{"ID":"4639874","Zeitstempel":"2023-11-1011:56:27.380","Zeitstempel_ms":"1699617387380","Zeitstempel_Unix_ms":"1699613787380","Druck":"7.04412","Durchfluss":"132.202","Temperatur1":"23.898","Temperatur2":"1372"}],"Kompressor_Ostfalia":[{"ID":"12205255","Zeitstempel":"2023-11-1011:56:27.310","Zeitstempel_ms":"1699617387310","Zeitstempel_Unix_ms":"1699613787310","Strom_gesamt":"0.06227877353748492","Spannung_gesamt":"399.2848229265921","Wirkleistung_gesamt":"13.650000000000002","Scheinleistung_gesamt":"25.107655195","Blindleistung_gesamt":"14.859715638930806","Energie_gesamt_kwh":"11108.303394999999","cosPhi_gesamt":"0.11099999999999999","Phi_gesamt":"0.6881213930770241","sinPhi_gesamt":"0.4912569731672557","Frequenz_gesamt":"50","Strom_Phase1":"0.08406999999999999","Spannung_Phase1":"230.20620000000002","Wirkleistung_Phase1":"17.150000000000002","Scheinleistung_Phase1":"19.474293489","Blindleistung_Phase1":"9.226353932930806","Energie_Phase1_kwh":"3909.048675","cosPhi_Phase1":"0.833","Phi_Phase1":"0.4935678524361759","sinPhi_Phase1":"0.47377091950176703","Frequenz_Phase1":"50","Strom_Phase2":"0","Spannung_Phase2":"230.45260000000002","Wirkleistung_Phase2":"0","Scheinleistung_Phase2":"0","Blindleistung_Phase2":"0","Energie_Phase2_kwh":"3635.096885","cosPhi_Phase2":"0","Phi_Phase2":"0","sinPhi_Phase2":"0","Frequenz_Phase2":"50","Strom_Phase3":"0.023799999999999998","Spannung_Phase3":"230.92280000000002","Wirkleistung_Phase3":"-3.5","Scheinleistung_Phase3":"5.6333617060000005","Blindleistung_Phase3":"5.6333617060000005","Energie_Phase3_kwh":"3564.157835","cosPhi_Phase3":"-0.5","Phi_Phase3":"1.5707963267948966","sinPhi_Phase3":"1","Frequenz_Phase3":"50"}]}



    def test_get_relevant_data(self):
        api_response_example = {"Kompressor_IPT":[{"ID":"12205254","Zeitstempel":"2023-11-10 11:56:27.410","Zeitstempel_ms":"1699617387410","Zeitstempel_Unix_ms":"1699613787410","Strom_gesamt":"0.029684464090384603","Spannung_gesamt":"399.5476327691272","Wirkleistung_gesamt":"10.15","Scheinleistung_gesamt":"12.133571225999999","Blindleistung_gesamt":"6.648387074803566","Energie_gesamt_kwh":"18988.191285","cosPhi_gesamt":"0.3333333333333333","Phi_gesamt":"0.19329719425651024","sinPhi_gesamt":"0.18264441553577956","Frequenz_gesamt":"50","Strom_Phase1":"0","Spannung_Phase1":"229.8694","Wirkleistung_Phase1":"0","Scheinleistung_Phase1":"0","Blindleistung_Phase1":"0","Energie_Phase1_kwh":"6054.99972","cosPhi_Phase1":"0","Phi_Phase1":"0","sinPhi_Phase1":"0","Frequenz_Phase1":"50","Strom_Phase2":"0","Spannung_Phase2":"230.5886","Wirkleistung_Phase2":"0","Scheinleistung_Phase2":"0","Blindleistung_Phase2":"0","Energie_Phase2_kwh":"6387.277785","cosPhi_Phase2":"0","Phi_Phase2":"0","sinPhi_Phase2":"0","Frequenz_Phase2":"50","Strom_Phase3":"0.051414999999999995","Spannung_Phase3":"231.5788","Wirkleistung_Phase3":"10.15","Scheinleistung_Phase3":"12.133571225999999","Blindleistung_Phase3":"6.648387074803566","Energie_Phase3_kwh":"6545.91378","cosPhi_Phase3":"1","Phi_Phase3":"0.5798915827695307","sinPhi_Phase3":"0.5479332466073387","Frequenz_Phase3":"50"}],"Kompressor_IPT_Entlueftung":[{"ID":"12203203","Zeitstempel":"2023-11-1011:56:27.390","Zeitstempel_ms":"1699617387390","Zeitstempel_Unix_ms":"1699613787390","Strom_gesamt":"0.013505000000000001","Spannung_gesamt":"230.59040000000002","Wirkleistung_gesamt":"1.44","Scheinleistung_gesamt":"3.0380285200000006","Blindleistung_gesamt":"2.675073323917196","Energie_gesamt_kwh":"36.17966","cosPhi_gesamt":"0.75","Phi_gesamt":"1.076977868369864","sinPhi_gesamt":"0.8805293651151094","Frequenz_gesamt":"50"}],"Kompressor_IPT_Kuehler":[{"ID":"12203200","Zeitstempel":"2023-11-1011:56:27.400","Zeitstempel_ms":"1699617387400","Zeitstempel_Unix_ms":"1699613787400","Strom_gesamt":"1.75798","Spannung_gesamt":"229.9522","Wirkleistung_gesamt":"251.99","Scheinleistung_gesamt":"403.84320340100004","Blindleistung_gesamt":"315.57942396991206","Energie_gesamt_kwh":"1008.193971","cosPhi_gesamt":"0.623","Phi_gesamt":"0.8969710172255206","sinPhi_gesamt":"0.7814404732139428","Frequenz_gesamt":"50"}],"Kompressor_IPT_Sensoren":[{"ID":"4639874","Zeitstempel":"2023-11-1011:56:27.380","Zeitstempel_ms":"1699617387380","Zeitstempel_Unix_ms":"1699613787380","Druck":"7.04412","Durchfluss":"132.202","Temperatur1":"23.898","Temperatur2":"1372"}],"Kompressor_Ostfalia":[{"ID":"12205255","Zeitstempel":"2023-11-1011:56:27.310","Zeitstempel_ms":"1699617387310","Zeitstempel_Unix_ms":"1699613787310","Strom_gesamt":"0.06227877353748492","Spannung_gesamt":"399.2848229265921","Wirkleistung_gesamt":"13.650000000000002","Scheinleistung_gesamt":"25.107655195","Blindleistung_gesamt":"14.859715638930806","Energie_gesamt_kwh":"11108.303394999999","cosPhi_gesamt":"0.11099999999999999","Phi_gesamt":"0.6881213930770241","sinPhi_gesamt":"0.4912569731672557","Frequenz_gesamt":"50","Strom_Phase1":"0.08406999999999999","Spannung_Phase1":"230.20620000000002","Wirkleistung_Phase1":"17.150000000000002","Scheinleistung_Phase1":"19.474293489","Blindleistung_Phase1":"9.226353932930806","Energie_Phase1_kwh":"3909.048675","cosPhi_Phase1":"0.833","Phi_Phase1":"0.4935678524361759","sinPhi_Phase1":"0.47377091950176703","Frequenz_Phase1":"50","Strom_Phase2":"0","Spannung_Phase2":"230.45260000000002","Wirkleistung_Phase2":"0","Scheinleistung_Phase2":"0","Blindleistung_Phase2":"0","Energie_Phase2_kwh":"3635.096885","cosPhi_Phase2":"0","Phi_Phase2":"0","sinPhi_Phase2":"0","Frequenz_Phase2":"50","Strom_Phase3":"0.023799999999999998","Spannung_Phase3":"230.92280000000002","Wirkleistung_Phase3":"-3.5","Scheinleistung_Phase3":"5.6333617060000005","Blindleistung_Phase3":"5.6333617060000005","Energie_Phase3_kwh":"3564.157835","cosPhi_Phase3":"-0.5","Phi_Phase3":"1.5707963267948966","sinPhi_Phase3":"1","Frequenz_Phase3":"50"}]}
        relevant_keys = {
            "Kompressor_IPT": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],
            "Kompressor_IPT_Entlueftung": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],
            "Kompressor_IPT_Kuehler": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],
            "Kompressor_IPT_Sensoren": ["ID", "Zeitstempel", "Druck", "Durchfluss", "Temperatur1"],
            "Kompressor_Ostfalia": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],
        }

        api_instance = Api()
        result = api_instance.get_relevant_data(api_response_example, relevant_keys)
        assert result == {'Kompressor_IPT': [{'Energie_gesamt_kwh': '18988.191285','ID': '12205254','Zeitstempel': '2023-11-10 11:56:27.410'}],'Kompressor_IPT_Entlueftung': [{'Energie_gesamt_kwh': '36.17966','ID': '12203203','Zeitstempel': '2023-11-1011:56:27.390'}],'Kompressor_IPT_Kuehler': [{'Energie_gesamt_kwh': '1008.193971','ID': '12203200','Zeitstempel': '2023-11-1011:56:27.400'}],'Kompressor_IPT_Sensoren': [{'Druck': '7.04412','Durchfluss': '132.202','ID': '4639874','Temperatur1': '23.898','Zeitstempel': '2023-11-1011:56:27.380'}],'Kompressor_Ostfalia': [{'Energie_gesamt_kwh': '11108.303394999999','ID': '12205255','Zeitstempel': '2023-11-1011:56:27.310'}]}

    def test_get_relevant_data_missing_kompressor(self):
        api_response_example = {"Kompressor_IPT": [
            {"ID": "12205254", "Zeitstempel": "2023-11-10 11:56:27.410", "Zeitstempel_ms": "1699617387410",
             "Zeitstempel_Unix_ms": "1699613787410", "Strom_gesamt": "0.029684464090384603",
             "Spannung_gesamt": "399.5476327691272", "Wirkleistung_gesamt": "10.15",
             "Scheinleistung_gesamt": "12.133571225999999", "Blindleistung_gesamt": "6.648387074803566",
             "Energie_gesamt_kwh": "18988.191285", "cosPhi_gesamt": "0.3333333333333333",
             "Phi_gesamt": "0.19329719425651024", "sinPhi_gesamt": "0.18264441553577956", "Frequenz_gesamt": "50",
             "Strom_Phase1": "0", "Spannung_Phase1": "229.8694", "Wirkleistung_Phase1": "0",
             "Scheinleistung_Phase1": "0", "Blindleistung_Phase1": "0", "Energie_Phase1_kwh": "6054.99972",
             "cosPhi_Phase1": "0", "Phi_Phase1": "0", "sinPhi_Phase1": "0", "Frequenz_Phase1": "50",
             "Strom_Phase2": "0", "Spannung_Phase2": "230.5886", "Wirkleistung_Phase2": "0",
             "Scheinleistung_Phase2": "0", "Blindleistung_Phase2": "0", "Energie_Phase2_kwh": "6387.277785",
             "cosPhi_Phase2": "0", "Phi_Phase2": "0", "sinPhi_Phase2": "0", "Frequenz_Phase2": "50",
             "Strom_Phase3": "0.051414999999999995", "Spannung_Phase3": "231.5788", "Wirkleistung_Phase3": "10.15",
             "Scheinleistung_Phase3": "12.133571225999999", "Blindleistung_Phase3": "6.648387074803566",
             "Energie_Phase3_kwh": "6545.91378", "cosPhi_Phase3": "1", "Phi_Phase3": "0.5798915827695307",
             "sinPhi_Phase3": "0.5479332466073387", "Frequenz_Phase3": "50"}], "Kompressor_IPT_Entlueftung": [
            {"ID": "12203203", "Zeitstempel": "2023-11-1011:56:27.390", "Zeitstempel_ms": "1699617387390",
             "Zeitstempel_Unix_ms": "1699613787390", "Strom_gesamt": "0.013505000000000001",
             "Spannung_gesamt": "230.59040000000002", "Wirkleistung_gesamt": "1.44",
             "Scheinleistung_gesamt": "3.0380285200000006", "Blindleistung_gesamt": "2.675073323917196",
             "Energie_gesamt_kwh": "36.17966", "cosPhi_gesamt": "0.75", "Phi_gesamt": "1.076977868369864",
             "sinPhi_gesamt": "0.8805293651151094", "Frequenz_gesamt": "50"}], "Kompressor_IPT_Kuehler": [
            {"ID": "12203200", "Zeitstempel": "2023-11-1011:56:27.400", "Zeitstempel_ms": "1699617387400",
             "Zeitstempel_Unix_ms": "1699613787400", "Strom_gesamt": "1.75798", "Spannung_gesamt": "229.9522",
             "Wirkleistung_gesamt": "251.99", "Scheinleistung_gesamt": "403.84320340100004",
             "Blindleistung_gesamt": "315.57942396991206", "Energie_gesamt_kwh": "1008.193971",
             "cosPhi_gesamt": "0.623", "Phi_gesamt": "0.8969710172255206", "sinPhi_gesamt": "0.7814404732139428",
             "Frequenz_gesamt": "50"}], "Kompressor_IPT_Sensoren": [
            {"ID": "4639874", "Zeitstempel": "2023-11-1011:56:27.380", "Zeitstempel_ms": "1699617387380",
             "Zeitstempel_Unix_ms": "1699613787380", "Druck": "7.04412", "Durchfluss": "132.202",
             "Temperatur1": "23.898", "Temperatur2": "1372"}]}

        relevant_keys = {
            "Kompressor_IPT": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],
            "Kompressor_IPT_Entlueftung": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],
            "Kompressor_IPT_Kuehler": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],
            "Kompressor_IPT_Sensoren": ["ID", "Zeitstempel", "Druck", "Durchfluss", "Temperatur1"],
            "Kompressor_Ostfalia": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],
        }

        api_instance = Api()
        result = api_instance.get_relevant_data(api_response_example, relevant_keys)
        assert result == {'Kompressor_IPT': [{'Energie_gesamt_kwh': '18988.191285','ID': '12205254','Zeitstempel': '2023-11-10 11:56:27.410'}],'Kompressor_IPT_Entlueftung': [{'Energie_gesamt_kwh': '36.17966','ID': '12203203','Zeitstempel': '2023-11-1011:56:27.390'}],'Kompressor_IPT_Kuehler': [{'Energie_gesamt_kwh': '1008.193971','ID': '12203200','Zeitstempel': '2023-11-1011:56:27.400'}],'Kompressor_IPT_Sensoren': [{'Druck': '7.04412','Durchfluss': '132.202','ID': '4639874','Temperatur1': '23.898','Zeitstempel': '2023-11-1011:56:27.380'}]}

    @patch("api.pymysql.connect")
    def test_connect_to_database_successful(self, mock_pymysql_connect):
        # Konfigurieren Sie das Mock-Verhalten
        mock_connection = mock_pymysql_connect.return_value

        # Erstellen Sie eine Instanz Ihrer API-Klasse
        api_instance = Api()

        # Führen Sie die Methode aus, die die Verbindung zur Datenbank herstellt
        result = api_instance.connect_to_database()

        # Überprüfen Sie, ob die pymysql.connect-Methode einmal aufgerufen wurde
        mock_pymysql_connect.assert_called_once_with(
            host='141.41.42.211',
            user='Kompressor',
            password='Kompressor12345%',
            database='kompressor',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        # Überprüfen Sie, ob die Verbindung korrekt zurückgegeben wurde
        assert result == mock_connection

    @patch("api.pymysql.connect")
    def test_connection_to_database_unsuccessfull(self, mock_pymysql_connect):
        # Konfigurieren Sie das Mock-Verhalten, um eine Ausnahme zu werfen
        mock_pymysql_connect.side_effect = pymysql.Error("Connection failed")

        # Erstellen Sie eine Instanz Ihrer API-Klasse
        api_instance = Api()

        # Führen Sie die Methode aus, die die Verbindung zur Datenbank herstellt
        result = api_instance.connect_to_database()

        # Überprüfen Sie, ob die pymysql.connect-Methode einmal aufgerufen wurde
        mock_pymysql_connect.assert_called_once_with(
            host='141.41.42.211',
            user='Kompressor',
            password='Kompressor12345%',
            database='kompressor',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        # Überprüfen Sie, ob die Verbindung nicht erfolgreich war und None zurückgegeben wurde
        assert result == None
