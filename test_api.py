'''
Kopfzeile

'''

from api import *
from unittest.mock import MagicMock, patch

class TestApi():

    def test_api_call_unsuccessful(self):
        mock_response = MagicMock()

        # Setzen Sie den gewünschten Statuscode
        mock_response.status_code = 404

        # Mocken Sie requests.get
        with patch("requests.get", return_value=mock_response):
            # Rufen Sie die Funktion auf, die requests.get verwendet
            api_instance = Api()
            result = api_instance.get_response_url("http://example.com")
        assert result == None

    @patch("api.requests.get")
    def test_get_response_url_successful(self, mock_requests_get):
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
    def test_connection_to_database_unsuccessful(self, mock_pymysql_connect):
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
