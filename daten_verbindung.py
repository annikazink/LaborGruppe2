"""datenverbindung"""
from unittest.mock import MagicMock
import pytest


# Beispielstruktur der Daten basierend auf den Informationen aus dem Bild
beispiel_kompressor_daten = {
    "Kompressor_IPT": {
        "ID": "12205254",
        "Zeitstempel": "2023-11-10 11:56:27.410",
        "Zeitstempel_Unix_ms": "1699613787410",
        "Strom_gesamt": "0.029684464090384603",
        "Spannung_gesamt": "399.5476327691272",
        "Wirkleistung_gesamt": "6.64837087403566",
        "Blindleistung_gesamt": "0",
        "Energie_gesamt_kwh": "18988.191285",
        "CosPhi_gesamt": "0.3333333333333333",
        "Frequenz_gesamt": "50.0",
        "Temperatur1": "23.898",
        "Temperatur2": "137.2",
        "Druck": "0.74412",
        "Durchfluss": "132.202"
        # Weitere Schlüssel-Werte hier hinzufügen, falls nötig
    }
}


# Funktion, die wir testen wollen, könnte so aussehen
def hole_kompressor_daten():
    """kompressor daten"""
    # Diese Funktion würde normalerweise die Daten von einem externen Server abrufen

@pytest.fixture
def mock_kompressor_daten(monkeypatch):
    """kompressor daten"""
    # Erstellen eines MagicMock-Objekts, das die simulierten Kompressordaten zurückgibt
    mock_datenquelle = MagicMock(return_value=beispiel_kompressor_daten)
    # Ersetzen der echten Funktion, die Daten abruft, durch den MagicMock
    monkeypatch.setattr("Daten.hole_kompressor_daten", mock_datenquelle)
    return (
        mock_datenquelle  # Wir geben das Mock-Objekt zurück für die Verwendung im Test
    )
