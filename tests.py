from daten_bereitstellen import merge_data, bearbeite_datensaetze

# Test für die Funktion `merge_data`
def test_merge_data():
    daten_geraet = [{'geraet_id': 1, 'datas_id': 1, 'zeitstempel': '2024-01-19 12:00:00'},
                    {'geraet_id': 1, 'datas_id': 2, 'zeitstempel': '2024-01-19 13:00:00'}]
    daten_sensor = [{'datas_id': 1, 'zeitstempel': '2024-01-19 12:00:00', 'druck': 100, 'durchfluss': 50},
                    {'datas_id': 2, 'zeitstempel': '2024-01-19 13:00:00', 'druck': 120, 'durchfluss': 60}]

    result = merge_data(daten_geraet, daten_sensor)

    # Test für die Funktion `merge_data`
    def test_merge_data():
        daten_geraet = [{'geraet_id': 1, 'datas_id': 1, 'zeitstempel': '2024-01-19 12:00:00'}]
        daten_sensor = [{'datas_id': 1, 'zeitstempel': '2024-01-19 12:00:00', 'druck': 100, 'durchfluss': 50}]

        result = merge_data(daten_geraet, daten_sensor)

        assert len(result) == 1
        assert result[0]['druck'] == 100  # Prüfen Sie, ob 'druck' im Ergebnis enthalten ist und den erwarteten Wert hat
        assert result[0]['durchfluss'] == 50
        assert result[0]['temperatur'] is None

# Test für die Funktion `bearbeite_datensaetze`
def test_bearbeite_datensaetze():
    daten_geraet = [{'geraet_id': 1, 'zeitstempel': '2024-01-19 12:00:00', 'energie': 50},
                    {'geraet_id': 2, 'zeitstempel': '2024-01-19 12:00:00', 'energie': 30},
                    {'geraet_id': 4, 'zeitstempel': '2024-01-19 12:00:00', 'energie': 10},
                    {'geraet_id': 1, 'zeitstempel': '2024-01-19 13:00:00', 'energie': 60}]

    result = bearbeite_datensaetze(daten_geraet)

    assert len(result) == 2
    assert result[0]['gesamt_energie'] == 80
    assert result[1]['gesamt_energie'] == 60

"""
def test_filter_data(self):
    #Testet, ob die Filterfunktion der Daten korrekt funktioniert.
    self.fail("Noch nicht implementiert")


def test_display_data_in_line_graph(self):
    #Testet, ob Daten korrekt in einem Liniendiagramm dargestellt werden.
    self.fail("Noch nicht implementiert")


def test_update_graph_on_data_change(self):
    #Testet, ob der Graph sich aktualisiert, wenn sich die zugrunde liegenden Daten ändern.
    self.fail("Noch nicht implementiert")


def test_gui_response_to_invalid_data(self):
    #Testet, ob die GUI korrekt auf ungültige Daten reagiert.
    #Hier würden Sie die GUI-Funktion aufrufen, die ungültige Daten verarbeitet
    #Dann überprüfen Sie, ob das Ergebnis Ihren Erwartungen entspricht
    self.fail("Noch nicht implementiert")


def test_error_message_display_for_missing_data(self):
    #Testet, ob Fehlermeldungen korrekt angezeigt werden, wenn Daten fehlen.
    #Hier würden Sie die GUI-Funktion aufrufen, die auf fehlende Daten reagiert
    #Dann überprüfen Sie, ob eine angemessene Fehlermeldung angezeigt wird
    self.fail("Noch nicht implementiert")
"""

import unittest
import tkinter as tk
from unittest.mock import MagicMock
from gui_entwurf import MainApp

class TestMainApp(unittest.TestCase):

    def setUp(self):
        self.app = MainApp()
        self.app.withdraw()  # Verhindert, dass das Hauptfenster während der Tests angezeigt wird

    def test_create_kompressor_ipt_page(self):
        kompressor_ipt_page = self.app.notebook.tab(0, "text")
        self.assertEqual(kompressor_ipt_page, "Kompressor IPT")

    def test_create_plus_page(self):
        plus_page = self.app.notebook.tab(2, "text")
        self.assertEqual(plus_page, "+")

    def test_add_device(self):
        # Mocken Sie die Benutzereingabe für den neuen Gerätenamen
        self.app.new_name_entry = MagicMock()
        self.app.new_name_entry.get.return_value = "NewDevice"

        # Mocken Sie die Datenbankverbindung
        self.app.connect_to_database = MagicMock()

        # Rufen Sie die Methode zum Hinzufügen des Geräts auf
        self.app.add_device()

        # Überprüfen Sie, ob die Methode zur Datenbankverbindung aufgerufen wurde
        self.app.connect_to_database.assert_called_once()

        # Überprüfen Sie, ob die Methode zum Hinzufügen des Geräts aufgerufen wurde
        self.assertTrue(self.app.new_name_entry.get.called)

    def test_show_kompressor_ipt_kompressor(self):
        # Mocken Sie die filter_and_plot_data-Funktion
        self.app.close_current_menu = MagicMock()
        self.app.filter_and_plot_data = MagicMock()

        # Rufen Sie die Methode zum Anzeigen des Kompressor-Bereichs auf
        self.app.show_kompressor_ipt_kompressor()

        # Überprüfen Sie, ob die Methode zum Schließen des aktuellen Menüs aufgerufen wurde
        self.assertTrue(self.app.close_current_menu.called)

        # Überprüfen Sie, ob die Methode filter_and_plot_data mit den richtigen Parametern aufgerufen wurde
        expected_config = {
            "device_id": 1,
            "days": 7,
            "x_label": "Zeit",
            "y_label": "Energie",
            "title": "Energieverlauf letzte 7 Tage",
            "x_key": "zeitstempel",
            "y_key": "energie",
        }
        self.app.filter_and_plot_data.assert_called_once_with(self.app.daten_komplett, expected_config)

    def test_show_kompressor_ipt_entluefter(self):
        # Ähnlich wie oben, testen Sie die Methode show_kompressor_ipt_entluefter

    # Fügen Sie weitere Testfälle für andere Methoden hinzu...

if __name__ == '__main__':
    unittest.main()
