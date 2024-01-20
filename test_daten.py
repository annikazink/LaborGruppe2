from daten_bereitstellen import merge_data, bearbeite_datensaetze

# Test für die Funktion `merge_data`
def test_merge_data():
    daten_geraet = [{'datag_id': 12289622, 'geraet_id': 1, 'bereich': 'NewDevice', 'zeitstempel': '2024-01-19 21:34:31', 'energie': 1, 'datas_id': 22, 'druck': 0.7, 'durchfluss': 300, 'temperatur': 17}]
    daten_sensor = [{'datas_id': 4738319, 'sensor_id': 1, 'zeitstempel': '2023-12-14 16:49:53', 'druck': 7, 'durchfluss': 50, 'temperatur': 20}]

    result = merge_data(daten_geraet, daten_sensor)

    assert len(result) == 1
    assert result[0]['druck'] is None  # Prüfen, ob 'druck' im Ergebnis enthalten ist und den erwarteten Wert hat
    assert result[0]['durchfluss'] is None
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