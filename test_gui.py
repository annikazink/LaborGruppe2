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

if __name__ == '__main__':
    unittest.main()
