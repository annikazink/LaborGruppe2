# ReadME LaborGruppe2

## Modul 1 Datenbank
Anforderungen: <br>
Entwurf und Implementierung einer relationalen Datenbank zur Speicherung von Daten von zwei Kompressoren in
zwei unterschiedlichen Bereichen.
- Erstellung eines ER-Modells.
- Definition von Tabellen und Beziehungen.
- Implementierung in SQL.
- Schreiben von Testfällen, um die korrekte Speicherung und Abfrage der Daten zu überprüfen.
- Erweiterbarkeit für weitere Geräte einplanen

ER-Modell der verwendeten Datenbank:
![image](https://github.com/annikazink/LaborGruppe2/assets/146918028/c04873bc-5062-4ddf-9070-d67f38121655)

## Modul 2 GUI
Anforderungen:<br>
Entwicklung einer grafischen Benutzeroberfläche (GUI), um die Daten der Kompressoren anzuzeigen und zu verwalten.
-Entwurf einer benutzerfreundlichen Oberfläche<br>
-Implementierung der GUI in Python<br>
-Anbindung der GUI an die Datenbank über die SChnittstellenfunktion des 1. Moduls<br>
-Aufbereitung von historischen Wochendaten, Tagesverbräuche und Darstellen auf der GUI<br>
-Automatisiertes Testen der Aufbereitungsfunktion; Manuelles Testen der GUI<br>

## Modul 3 Schnittstelle
Anforderungen:<br>
Entwicklung eines Schnittstellenprogramms zur Kommunikation mit den Kompressoren über eine JSON-Web Schnittstelle.
- Implementierung einer API in Python, die die Daten von den Kompressoren empfängt und zyklisch an die Datenbank weiterleitet.
- Verarbeitung, Reduzierung und Normalisierung der eingehenden Daten.
- Schreiben von Mock-Tests zur Simulation der Kompressordaten und Überprüfung der Schnittstelle.
- Sicherstellung, dass die Schnittstelle robust und fehlertolerant ist.
