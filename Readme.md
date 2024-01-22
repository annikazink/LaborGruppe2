# ReadME LaborGruppe2

## Vorwort
Für die Bewertung des Codes sind die einzelnen Branches entscheidend, da sich in ihnen sowohl der Code, als auch die Tests befinden. Die Main bildet lediglich den Produktivcode nochmal sauber ab, entscheidend ist hier jedoch nur die ReadMe Datei.

## Namen Übersetzung
daze1610 - David Zeiser 70481999 <br>
jelleneumann - Jelle Neumann 70482166 <br>
mxmkzk - Maxim Kozik 70481254 <br>
H4uMichBl4u - Hannes Kamann 70481032 <br>
annikazink - Annika Zink 70480872 <br>
martenweiser - Marten Weiser 70482937 <br>
bendokat123 - Constantin Bendokat 70475310 <br>

## User-Stories (Programmanforderungen)
Als Nutzer möchte ich, …<br>
- eine Bereichsauswahl in der GUI haben, um die angeschlossenen Geräte und deren Sensoren einzusehen.
- den Energieverbrauch der letzten sieben Tage und der letzten 24 Stunden direkt auf der GUI angezeigt bekommen.
- dass die Minimal-, Maximal- und Durchschnittstemperaturen der letzten sieben Tage und der letzten 24 Stunden sichtbar sind.
- die aktuellen Messwerte auf der GUI einsehen können
- den Verlauf der Temperatur und des Systemdrucks der letzten 24 Stunden in Form eines Diagramms darstellen lassen.
- auch historische Daten einsehen können. Die Daten sollen zyklisch aufbereitet und gespeichert werden.

## Modul 1 Datenbank
Jelle Neumann und David Zeiser<br>
#### Anforderungen: <br>
Entwurf und Implementierung einer relationalen Datenbank zur Speicherung von Daten von zwei Kompressoren in
zwei unterschiedlichen Bereichen.
- Erstellung eines ER-Modells.
- Definition von Tabellen und Beziehungen.
- Implementierung in SQL.
- Schreiben von Testfällen, um die korrekte Speicherung und Abfrage der Daten zu überprüfen.
- Erweiterbarkeit für weitere Geräte einplanen
  
#### ER-Modell Version 1:

![image](https://github.com/annikazink/LaborGruppe2/assets/146163637/d1276622-6574-4109-9ab6-8059ee2d3825)


#### ER-Modell (Version 2) der verwendeten Datenbank:

![image](https://github.com/annikazink/LaborGruppe2/assets/146163637/f84ea980-6a49-4c04-9e18-7e9cb9804e10)




## Modul 2 GUI
Annika Zink, Marten Weiser und Constantin Bendokat<br>
#### Anforderungen:<br>
Entwicklung einer grafischen Benutzeroberfläche (GUI), um die Daten der Kompressoren anzuzeigen und zu verwalten.
-Entwurf einer benutzerfreundlichen Oberfläche<br>
-Implementierung der GUI in Python<br>
-Anbindung der GUI an die Datenbank über die SChnittstellenfunktion des 1. Moduls<br>
-Aufbereitung von historischen Wochendaten, Tagesverbräuche und Darstellen auf der GUI<br>
-Automatisiertes Testen der Aufbereitungsfunktion; Manuelles Testen der GUI<br>

### CODE Review:

![image](https://github.com/annikazink/LaborGruppe2/assets/146163260/e7c7781e-d52d-44d0-8be6-95a42a550651)

![image](https://github.com/annikazink/LaborGruppe2/assets/146163637/9ba3a13a-1309-4995-a843-1abf2051eda8)

![image](https://github.com/annikazink/LaborGruppe2/assets/146163637/a77237c7-f73c-4a4c-8425-a6b9c9bb7a04)


## Modul 3 Schnittstelle
Hannes Kamann und Maxim Kozik<br>
#### Anforderungen:<br>
Entwicklung eines Schnittstellenprogramms zur Kommunikation mit den Kompressoren über eine JSON-Web Schnittstelle.
- Implementierung einer API in Python, die die Daten von den Kompressoren empfängt und zyklisch an die Datenbank weiterleitet.
- Verarbeitung, Reduzierung und Normalisierung der eingehenden Daten.
- Schreiben von Mock-Tests zur Simulation der Kompressordaten und Überprüfung der Schnittstelle.
- Sicherstellung, dass die Schnittstelle robust und fehlertolerant ist.

### Code Review:
![image](https://github.com/annikazink/LaborGruppe2/assets/146163637/e728d204-44ad-4591-8f87-e54c44e88d4b)

![image](https://github.com/annikazink/LaborGruppe2/assets/146163637/8818df6e-6ac3-4a0b-bd8f-b997fc821064)

![image](https://github.com/annikazink/LaborGruppe2/assets/146163637/65c39044-a909-4877-a943-b9720c57de9f)
