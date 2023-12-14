# ReadME LaborGruppe2

## User-Stories (Programmanforderungen)
Als Nutzer möchte ich, …<br>
- eine Bereichsauswahl in der GUI haben, um die angeschlossenen Geräte und deren Sensoren einzusehen.
- den Energieverbrauch der letzten sieben Tage und der letzten 24 Stunden direkt auf der GUI angezeigt bekommen.
- dass die Minimal-, Maximal- und Durchschnittstemperaturen der letzten sieben Tage und der letzten 24 Stunden sichtbar sind.
- die aktuellen Messwerte auf der GUI einsehen können
- den Verlauf der Temperatur und des Systemdrucks der letzten 24 Stunden in Form eines Diagramms darstellen lassen.
- auch historische Daten einsehen können. Die Daten sollen zyklisch aufbereitet und gespeichert werden.

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
![image](https://github.com/annikazink/LaborGruppe2/assets/146918028/e29cd336-864f-47c9-9820-9f6224623b1f)


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
