from daten_bereitstellen import merge_data, bearbeite_datensaetze


# Test für die Funktion `merge_data`
def test_merge_data():
    daten_geraet = [
        {
            "datag_id": 12289622,
            "geraet_id": 1,
            "bereich": "NewDevice",
            "zeitstempel": "2024-01-19 21:34:31",
            "energie": 1,
            "datas_id": 22,
            "druck": 0.7,
            "durchfluss": 300,
            "temperatur": 17,
        }
    ]
    daten_sensor = [
        {
            "datas_id": 4738319,
            "sensor_id": 1,
            "zeitstempel": "2023-12-14 16:49:53",
            "druck": 7,
            "durchfluss": 50,
            "temperatur": 20,
        }
    ]

    result = merge_data(daten_geraet, daten_sensor)

    assert len(result) == 1
    assert (
        result[0]["druck"] == None
    )  # Prüfen, ob 'druck' im Ergebnis enthalten ist und den erwarteten Wert hat
    assert result[0]["durchfluss"] == None
    assert result[0]["temperatur"] is None


# Test für die Funktion `bearbeite_datensaetze`
def test_bearbeite_datensaetze():
    daten_geraet = [
        {"geraet_id": 1, "zeitstempel": "2024-01-19 12:00:00", "energie": 50},
        {"geraet_id": 2, "zeitstempel": "2024-01-19 12:00:00", "energie": 30},
        {"geraet_id": 4, "zeitstempel": "2024-01-19 12:00:00", "energie": 10},
        {"geraet_id": 1, "zeitstempel": "2024-01-19 13:00:00", "energie": 60},
    ]

    result = bearbeite_datensaetze(daten_geraet)

    assert len(result) == 2
    assert result[0]["gesamt_energie"] == 80
    assert result[1]["gesamt_energie"] == 60


import unittest
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
        # Mocken der Benutzereingabe für den neuen Gerätenamen
        self.app.new_name_entry = MagicMock()
        self.app.new_name_entry.get.return_value = "NewDevice"

        # Mocken der Datenbankverbindung
        self.app.connect_to_database = MagicMock()

        # Aufrufen der Methode zum Hinzufügen des Geräts auf
        self.app.add_device()

        # Überprüfen, ob die Methode zum Hinzufügen des Geräts aufgerufen wurde
        self.assertTrue(self.app.new_name_entry.get.called)

    def test_show_kompressor_ipt_kompressor(self):
        # Mocken der filter_and_plot_data-Funktion
        self.app.close_current_menu = MagicMock()
        self.app.filter_and_plot_data = MagicMock()

        # Aufrufen der Methode zum Anzeigen des Kompressor-Bereichs auf
        self.app.show_kompressor_ipt_kompressor()

        # Überprüfen, ob die Methode zum Schließen des aktuellen Menüs aufgerufen wurde
        self.assertTrue(self.app.close_current_menu.called)


if __name__ == "__main__":
    unittest.main()
