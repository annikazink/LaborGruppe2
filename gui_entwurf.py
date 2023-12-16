"""
Modul zur Verwaltung und Visualisierung von Kompressordaten mit Tkinter und Matplotlib.

Dieses Modul beinhaltet die Klasse MainApp, die eine umfassende grafische Benutzeroberfläche (GUI)
 für die Überwachung
und Analyse von Kompressordaten erstellt. Sie ermöglicht es Benutzern,
 verschiedene Datenansichten für Kompressoren
bei IPT und Ostfalia einzusehen, einschließlich aktueller und historischer Daten.
 Die Anwendung nutzt Tkinter für die
GUI und Matplotlib für die Datenvisualisierung. Es können wichtige Metriken
 wie Energieverbrauch, Druck, Temperatur
und Durchfluss über unterschiedliche Zeiträume hinweg visualisiert werden.

Die Variable 'alledrei' dient als eine Sammlung von IDs, die für die Filterung
 und Analyse aller drei Hauptkomponenten
der Kompressordaten verwendet wird.

Hauptfunktionen:
- Erstellen von Benutzeroberflächen für verschiedene Kompressordatenansichten.
- Filtern von Daten nach Geräte-ID und Zeitraum.
- Visualisierung von Daten in Diagrammen mit Matplotlib.

Wichtige Importe:
- tkinter: Für die GUI-Komponenten.
- datetime: Zum Umgang mit Datums- und Zeitdaten.
- matplotlib: Zur Erstellung von Diagrammen zur Datenvisualisierung.
"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
alledrei = [1,2,3]

# Beispielaufruf der Funktionen
daten_komplett = [
    {'datag_id': 1, 'geraet_id': 1, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-01 08:00:00',
     'energie': 100,
     'datas_id': 101},
    {'datag_id': 2, 'geraet_id': 2, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-02 09:30:00',
     'energie': 150,
     'datas_id': 102},
    {'datag_id': 3, 'geraet_id': 3, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-03 10:45:00',
     'energie': 120,
     'datas_id': 103},
    {'datag_id': 4, 'geraet_id': 4, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-04 11:15:00',
     'energie': 130,
     'datas_id': 104},
    {'datag_id': 5, 'geraet_id': 1, 'bereich': 'Bereich C', 'zeitstempel': '2023-12-05 12:30:00',
     'energie': 110,
     'datas_id': 105},
    {'datag_id': 6, 'geraet_id': 2, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-06 13:45:00',
     'energie': 140,
     'datas_id': 106},
    {'datag_id': 7, 'geraet_id': 3, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-07 14:55:00',
     'energie': 125,
     'datas_id': 107},
    {'datag_id': 8, 'geraet_id': 4, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-08 15:20:00',
     'energie': 155,
     'datas_id': 108},
    {'datag_id': 9, 'geraet_id': 1, 'bereich': 'Bereich C', 'zeitstempel': '2023-12-09 16:40:00',
     'energie': 145,
     'datas_id': 109},
    {'datag_id': 10, 'geraet_id': 2, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-10 17:10:00',
     'energie': 135,
     'datas_id': 110},
    {'datag_id': 11, 'geraet_id': 3, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-11 18:25:00',
     'energie': 115,
     'datas_id': 111},
    {'datag_id': 12, 'geraet_id': 4, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-12 19:40:00',
     'energie': 125,
     'datas_id': 112},
    {'datag_id': 13, 'geraet_id': 1, 'bereich': 'Bereich C', 'zeitstempel': '2023-12-13 20:50:00',
     'energie': 105,
     'datas_id': 113},
    {'datag_id': 14, 'geraet_id': 2, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-14 21:15:00',
     'energie': 150,
     'datas_id': 114},
    {'datag_id': 15, 'geraet_id': 3, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-15 22:30:00',
     'energie': 140,
     'datas_id': 115},
    {'datag_id': 16, 'geraet_id': 4, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-16 23:45:00',
     'energie': 130,
     'datas_id': 116},
    {'datag_id': 17, 'geraet_id': 1, 'bereich': 'Bereich C', 'zeitstempel': '2023-12-17 14:55:00',
     'energie': 110,
     'datas_id': 117},
    {'datag_id': 18, 'geraet_id': 2, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-18 01:10:00',
     'energie': 135,
     'datas_id': 118},
    {'datag_id': 19, 'geraet_id': 3, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-19 02:25:00',
     'energie': 125,
     'datas_id': 119},
    {'datag_id': 20, 'geraet_id': 4, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-20 03:30:00',
     'energie': 160,
     'datas_id': 120},
    {'datag_id': 21, 'geraet_id': 1, 'bereich': 'Bereich C', 'zeitstempel': '2023-12-21 04:45:00',
     'energie': 115,
     'datas_id': 121},
    {'datag_id': 22, 'geraet_id': 2, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-22 05:55:00',
     'energie': 105,
     'datas_id': 122},
    {'datag_id': 23, 'geraet_id': 3, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-23 06:10:00',
     'energie': 140,
     'datas_id': 123},
    {'datag_id': 24, 'geraet_id': 4, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-24 07:25:00',
     'energie': 150,
     'datas_id': 124},
    {'datag_id': 25, 'geraet_id': 1, 'bereich': 'Bereich C', 'zeitstempel': '2023-12-25 08:35:00',
     'energie': 120,
     'datas_id': 125},
    {'datag_id': 26, 'geraet_id': 4, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-15 09:50:00',
     'energie': 110,
     'datas_id': 126},
    {'datag_id': 27, 'geraet_id': 3, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-27 10:05:00',
     'energie': 130,
     'datas_id': 127},
    {'datag_id': 28, 'geraet_id': 4, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-28 11:20:00',
     'energie': 140,
     'datas_id': 128},
    {'datag_id': 29, 'geraet_id': 1, 'bereich': 'Bereich C', 'zeitstempel': '2023-12-29 12:30:00',
     'energie': 150,
     'datas_id': 129},
    {'datag_id': 30, 'geraet_id': 2, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-30 13:45:00',
     'energie': 160,
     'datas_id': 130},
    {'datag_id': 31, 'geraet_id': 1, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-01 08:00:00',
     'energie': 110,
     'datas_id': 131},
    {'datag_id': 32, 'geraet_id': 2, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-02 09:30:00',
     'energie': 120,
     'datas_id': 132},
    {'datag_id': 33, 'geraet_id': 3, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-03 10:45:00',
     'energie': 130,
     'datas_id': 133},
    {'datag_id': 34, 'geraet_id': 4, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-04 11:15:00',
     'energie': 140,
     'datas_id': 134},
    {'datag_id': 35, 'geraet_id': 1, 'bereich': 'Bereich C', 'zeitstempel': '2023-12-05 12:30:00',
     'energie': 150,
     'datas_id': 135},
    {'datag_id': 36, 'geraet_id': 2, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-06 13:45:00',
     'energie': 160,
     'datas_id': 136},
    {'datag_id': 37, 'geraet_id': 3, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-07 14:55:00',
     'energie': 110,
     'datas_id': 137},
    {'datag_id': 38, 'geraet_id': 4, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-08 15:20:00',
     'energie': 120,
     'datas_id': 138},
    {'datag_id': 39, 'geraet_id': 1, 'bereich': 'Bereich C', 'zeitstempel': '2023-12-09 16:40:00',
     'energie': 130,
     'datas_id': 139},
    {'datag_id': 40, 'geraet_id': 2, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-10 17:10:00',
     'energie': 140,
     'datas_id': 140},
    {'datag_id': 41, 'geraet_id': 3, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-11 18:25:00',
     'energie': 150,
     'datas_id': 141},
    {'datag_id': 42, 'geraet_id': 4, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-12 19:40:00',
     'energie': 110,
     'datas_id': 142},
    {'datag_id': 43, 'geraet_id': 1, 'bereich': 'Bereich C', 'zeitstempel': '2023-12-13 20:50:00',
     'energie': 120,
     'datas_id': 143},
    {'datag_id': 44, 'geraet_id': 2, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-14 21:15:00',
     'energie': 130,
     'datas_id': 144},
    {'datag_id': 45, 'geraet_id': 3, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-15 22:30:00',
     'energie': 140,
     'datas_id': 145},
    {'datag_id': 46, 'geraet_id': 4, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-16 23:45:00',
     'energie': 150,
     'datas_id': 146},
    {'datag_id': 47, 'geraet_id': 1, 'bereich': 'Bereich C', 'zeitstempel': '2023-12-17 14:55:00',
     'energie': 160,
     'datas_id': 147},
    {'datag_id': 48, 'geraet_id': 2, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-18 01:10:00',
     'energie': 110,
     'datas_id': 148},
    {'datag_id': 49, 'geraet_id': 3, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-19 02:25:00',
     'energie': 120,
     'datas_id': 149},
    {'datag_id': 50, 'geraet_id': 4, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-20 03:30:00',
     'energie': 130,
     'datas_id': 150},
    {'datag_id': 51, 'geraet_id': 1, 'bereich': 'Bereich C', 'zeitstempel': '2023-12-21 04:45:00',
     'energie': 140,
     'datas_id': 151},
    {'datag_id': 52, 'geraet_id': 2, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-22 05:55:00',
     'energie': 150,
     'datas_id': 152},
    {'datag_id': 53, 'geraet_id': 3, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-23 06:10:00',
     'energie': 160,
     'datas_id': 153},
    {'datag_id': 54, 'geraet_id': 4, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-24 07:25:00',
     'energie': 110,
     'datas_id': 154},
    {'datag_id': 55, 'geraet_id': 1, 'bereich': 'Bereich C', 'zeitstempel': '2023-12-25 08:35:00',
     'energie': 120,
     'datas_id': 155},
    {'datag_id': 56, 'geraet_id': 4, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-26 09:50:00',
     'energie': 130,
     'datas_id': 156},
    {'datag_id': 57, 'geraet_id': 3, 'bereich': 'Bereich B', 'zeitstempel': '2023-12-27 10:05:00',
     'energie': 140,
     'datas_id': 157},
    {'datag_id': 58, 'geraet_id': 4, 'bereich': 'Bereich A', 'zeitstempel': '2023-12-28 11:20:00',
     'energie': 150,
     'datas_id': 158},
    {'datag_id': 59, 'geraet_id': 1, 'bereich': 'Bereich C', 'zeitstempel': '2023-12-29 12:30:00',
     'energie': 160,
     'datas_id': 159},

]  # Ihre vollständigen Daten

class MainApp(tk.Tk):
    """
        Hauptanwendung zur Verwaltung und Anzeige von Kompressordaten.

        Diese Anwendung bietet eine grafische Benutzeroberfläche zur Überwachung
         und Analyse der Leistung von Kompressoren.
        Sie umfasst Funktionen zur Ansicht verschiedener Datenaspekte der Kompressoren
         bei IPT und Ostfalia. Benutzer können
        aktuelle und historische Daten einsehen und Metriken wie Energieverbrauch, Druck,
         Temperatur und Durchflussrate
        über verschiedene Zeiträume hinweg visualisieren.
        """
    def __init__(self):
        super().__init__()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(padx=10, pady=10)

        # Erstelle die Seiten für Kompressor IPT und Kompressor Ostfalia
        self.create_kompressor_ipt_page()
        self.create_kompressor_ostfalia_page()

        self.current_menu_frame = None  # Initialisiere die current_menu_frame-Variable
        self.menu_frames = {}  # Initialisiere das menu_frames-Dictionary


    def create_kompressor_ipt_page(self):
        '''
                Erstellt die Benutzeroberfläche für den Kompressor IPT.
                Diese Methode initialisiert und platziert Schaltflächen
                 zur Darstellung verschiedener Datenansichten
                des Kompressors IPT, einschließlich Kompressor, Entlüfter,
                 Kühler und Gesamtdaten'''
        kompressor_ipt_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ipt_frame, text="Kompressor IPT")

        # Schaltflächen zum Anzeigen verschiedener Datenansichten
        tk.Button(
            kompressor_ipt_frame,
            text="Kompressor",
            command=self.show_kompressor_ipt_kompressor,
        ).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(
            kompressor_ipt_frame,
            text="Entluefter",
            command=self.show_kompressor_ipt_entluefter,
        ).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(
            kompressor_ipt_frame,
            text="Kuehler",
            command=self.show_kompressor_ipt_kuehler,
        ).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(
            kompressor_ipt_frame, text="Gesamt", command=self.show_kompressor_ipt_gesamt
        ).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(
            kompressor_ipt_frame,
            text="Historische Daten",
            command=self.show_kompressor_ipt_historische_daten,
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def create_kompressor_ostfalia_page(self):
        """
                Erstellt die Benutzeroberfläche für den Kompressor Ostfalia.
                Diese Methode fügt Schaltflächen hinzu, um verschiedene Datenansichten
                 für den Kompressor Ostfalia anzuzeigen,
                einschließlich Energieverbrauch und historischen Daten.
                """
        kompressor_ostfalia_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ostfalia_frame, text="Kompressor Ostfalia")

        # Schaltflächen zum Anzeigen verschiedener Datenansichten für Ostfalia
        tk.Button(
            kompressor_ostfalia_frame,
            text="Energieverbrauch",
            command=self.show_kompressor_ostfalia_energieverbrauch,
        ).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(
            kompressor_ostfalia_frame,
            text="Historische Daten",
            command=self.show_kompressor_ostfalia_historische_daten,
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def close_current_menu(self):
        """
                Schließt das aktuell geöffnete Menü.
                Falls ein Menü-Frame vorhanden ist, wird dieses zerstört und
                 die entsprechende Variable zurückgesetzt.
                """
        if self.current_menu_frame:
            self.current_menu_frame.destroy()
            self.current_menu_frame = None

    def filter_data_by_period(self, data_array, days):
        """
            Filtert die Daten, um nur die Einträge der letzten angegebenen Tage zurückzugeben.
            """

        current_time = datetime.now()
        threshold_time = current_time - timedelta(days=days)
        return [record for record in data_array if
                datetime.strptime(record['zeitstempel'], '%Y-%m-%d %H:%M:%S') > threshold_time]

    def filter_data_by_device_id(self, data_array, device_id):
        """
            Filtert die Daten basierend auf der angegebenen Geräte-ID.
            """

        return [record for record in data_array if record['geraet_id'] == device_id]

    def plot_data(self, data_array, x_label='X-Achse', y_label='Y-Achse', title='Diagramm',
                  x_key='zeitstempel', y_key='energie'):
        """
            Erstellt ein Diagramm aus den bereitgestellten Daten, wobei Beschriftungen
            und Titel angepasst werden können.
            """
        data_array.sort(key=lambda x: datetime.strptime(x[x_key], '%Y-%m-%d %H:%M:%S'))
        x_data = [datetime.strptime(record[x_key], '%Y-%m-%d %H:%M:%S') for record in data_array]
        y_data = [record[y_key] for record in data_array]

        plt.figure(figsize=(10, 6))
        plt.plot(x_data, y_data, marker='o', linestyle='-', color='b')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        axis = plt.gca()
        axis.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y\n%H:%M'))
        axis.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        plt.grid()
        plt.tight_layout()
        plt.xticks(rotation=45)
        plt.show()

    def filter_and_plot_data(self, data_array, config):
        """
            Kombiniert das Filtern der Daten nach Geräte-ID und Zeitraum
             mit der Erstellung eines Diagramms.
            """
        device_id = config.get('device_id')
        days = config.get('days')
        x_label = config.get('x_label', 'X-Achse')
        y_label = config.get('y_label', 'Y-Achse')
        title = config.get('title', 'Diagramm')
        x_key = config.get('x_key', 'zeitstempel')
        y_key = config.get('y_key', 'energie')

        filtered_data = self.filter_data_by_device_id(data_array, device_id)
        filtered_data = self.filter_data_by_period(filtered_data, days)
        self.plot_data(filtered_data, x_label, y_label, title, x_key, y_key)

    def show_kompressor_ipt_kompressor(self):
        """
                Zeigt die Benutzeroberfläche für den Kompressor-Bereich des IPT.
                Nutzer können hier Datenansichten für verschiedene Zeiträume wählen,
                 wie die letzten 7 Tage oder die letzten 24 Stunden.
                """
        self.close_current_menu()
        kompressordaten_ipt_frame = tk.Frame(self)
        kompressordaten_ipt_frame.pack(padx=10, pady=10)
        self.menu_frames["KompressordatenIPT"] = kompressordaten_ipt_frame
        self.current_menu_frame = kompressordaten_ipt_frame

        config_7_days = {
            'device_id': 1,
            'days': 7,
            'x_label': 'Zeit',
            'y_label': 'Energie',
            'title': 'Energieverlauf letzte 7 Tage',
            'x_key': 'zeitstempel',
            'y_key': 'energie'
        }

        tk.Button(
            kompressordaten_ipt_frame,
            text="7 Tage",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_7_days),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        config_24_hours = {
            'device_id': 1,
            'days': 1,
            'x_label': 'Zeit',
            'y_label': 'Energie',
            'title': 'Energieverlauf letzte 24 Stunden',
            'x_key': 'zeitstempel',
            'y_key': 'energie'
        }

        tk.Button(
            kompressordaten_ipt_frame,
            text="24h",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_24_hours),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            kompressordaten_ipt_frame, text="Zurück", command=self.close_current_menu
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_kompressor_ipt_entluefter(self):
        """
        Zeigt die Benutzeroberfläche für den Entlüfter des Kompressors IPT.
        """
        self.close_current_menu()
        entluefter_ipt_frame = tk.Frame(self)
        entluefter_ipt_frame.pack(padx=10, pady=10)
        self.current_menu_frame = entluefter_ipt_frame

        # Konfiguration für 7 Tage
        config_7_days = {
            'device_id': 2,
            'days': 7,
            'x_label': 'Zeit',
            'y_label': 'Energie',
            'title': 'Energieverlauf Entlüfter 7 Tage',
            'x_key': 'zeitstempel',
            'y_key': 'energie'
        }
        tk.Button(
            entluefter_ipt_frame,
            text="7 Tage",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_7_days),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Konfiguration für 24 Stunden
        config_24_hours = {
            'device_id': 2,
            'days': 1,
            'x_label': 'Zeit',
            'y_label': 'Energie',
            'title': 'Energieverlauf Entlüfter 24 Stunden',
            'x_key': 'zeitstempel',
            'y_key': 'energie'
        }
        tk.Button(
            entluefter_ipt_frame,
            text="24h",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_24_hours),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            entluefter_ipt_frame, text="Zurück", command=self.close_current_menu
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_kompressor_ipt_kuehler(self):
        """
        Zeigt die Benutzeroberfläche für den Kühler des Kompressors IPT.
        """
        self.close_current_menu()
        kuehler_ipt_frame = tk.Frame(self)
        kuehler_ipt_frame.pack(padx=10, pady=10)
        self.current_menu_frame = kuehler_ipt_frame

        # Konfiguration für 7 Tage
        config_7_days = {
            'device_id': 3,
            'days': 7,
            'x_label': 'Zeit',
            'y_label': 'Energie',
            'title': 'Energieverlauf Kühler letzte 7 Tage',
            'x_key': 'zeitstempel',
            'y_key': 'energie'
        }
        tk.Button(
            kuehler_ipt_frame,
            text="7 Tage",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_7_days),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Konfiguration für 24 Stunden
        config_24_hours = {
            'device_id': 3,
            'days': 1,
            'x_label': 'Zeit',
            'y_label': 'Energie',
            'title': 'Energieverlauf Kühler letzte 24 Stunden',
            'x_key': 'zeitstempel',
            'y_key': 'energie'
        }
        tk.Button(
            kuehler_ipt_frame,
            text="24h",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_24_hours),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            kuehler_ipt_frame, text="Zurück", command=self.close_current_menu
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_kompressor_ipt_gesamt(self):
        """
        Zeigt die Benutzeroberfläche für die Gesamtansicht des Kompressors IPT.
        """
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        gesamt_ipt_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        gesamt_ipt_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        self.current_menu_frame = (
            gesamt_ipt_frame  # Aktualisiert das aktuell geöffnete Menü
        )

        # Schaltflächen zum Anzeigen von verschiedenen Datenansichten
        tk.Button(
            gesamt_ipt_frame,
            text="Druck",
            command=self.show_gesamt_druck,
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            gesamt_ipt_frame,
            text="Durchfluss",
            command=self.show_gesamt_durchfluss,
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            gesamt_ipt_frame,
            text="Temperatur",
            command=self.show_gesamt_temperatur,
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            gesamt_ipt_frame,
            text="Energie",
            command=self.show_gesamt_energie,
        ).pack(pady=5, padx=10, side=tk.LEFT)


        tk.Button(
            gesamt_ipt_frame, text="Zurück", command=self.close_current_menu
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_kompressor_ipt_historische_daten(self):
        """
        Zeigt die Benutzeroberfläche für historische Daten des Kompressors IPT.
        """
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        historische_daten_ipt_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        historische_daten_ipt_frame.pack(
            padx=10, pady=10
        )  # Platziert den Frame im Hauptfenster
        self.current_menu_frame = (
            historische_daten_ipt_frame  # Aktualisiert das aktuell geöffnete Menü
        )

        # Schaltflächen zum Anzeigen von verschiedenen Datenansichten
        tk.Button(
            historische_daten_ipt_frame,
            text="Druck",
            command=self.show_historische_daten_druck,
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            historische_daten_ipt_frame,
            text="Durchfluss",
            command=self.show_historische_daten_durchfluss,
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            historische_daten_ipt_frame,
            text="Temperatur",
            command=self.show_historische_daten_temperatur,
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            historische_daten_ipt_frame,
            text="Energie",
            command=self.show_historische_daten_energie,
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(
            historische_daten_ipt_frame, text="Zurück", command=self.close_current_menu,
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_kompressor_ostfalia_energieverbrauch(self):
        """
        Zeigt die Benutzeroberfläche für den Energieverbrauch des Kompressors Ostfalia.
        """
        self.close_current_menu()
        energieverbrauch_ostfalia_frame = tk.Frame(self)
        energieverbrauch_ostfalia_frame.pack(padx=10, pady=10)
        self.current_menu_frame = energieverbrauch_ostfalia_frame

        # Konfiguration für 7 Tage
        config_7_days = {
            'device_id': 4,
            'days': 7,
            'x_label': 'Zeit',
            'y_label': 'Energie',
            'title': 'Energieverlauf letzte 7 Tage',
            'x_key': 'zeitstempel',
            'y_key': 'energie'
        }
        tk.Button(
            energieverbrauch_ostfalia_frame,
            text="7 Tage",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_7_days),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Konfiguration für 24 Stunden
        config_24_hours = {
            'device_id': 4,
            'days': 1,
            'x_label': 'Zeit',
            'y_label': 'Energie',
            'title': 'Energieverlauf letzte 24 Stunden',
            'x_key': 'zeitstempel',
            'y_key': 'energie'
        }
        tk.Button(
            energieverbrauch_ostfalia_frame,
            text="24h",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_24_hours),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            energieverbrauch_ostfalia_frame, text="Zurück", command=self.close_current_menu
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_kompressor_ostfalia_historische_daten(self):
        """
        Zeigt die Benutzeroberfläche für historische Daten des Kompressors Ostfalia.
        """
        self.close_current_menu()
        historische_daten_ostfalia_frame = tk.Frame(self)
        historische_daten_ostfalia_frame.pack(padx=10, pady=10)
        self.current_menu_frame = historische_daten_ostfalia_frame

        # Konfiguration für die historischen Energie-Daten
        config_historische_daten = {
            'device_id': 4,
            'days': '',
            'x_label': 'Zeit',
            'y_label': 'Energie',
            'title': 'Historischer Energieverlauf',
            'x_key': 'zeitstempel',
            'y_key': 'energie'
        }
        tk.Button(
            historische_daten_ostfalia_frame,
            text="Energie",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_historische_daten),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(
            historische_daten_ostfalia_frame,
            text="Zurück",
            command=self.close_current_menu,
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_gesamt_druck(self):
        """
        Zeigt die Benutzeroberfläche für die Gesamtdruckansicht des Kompressors
        mit verschiedenen Zeitoptionen.
        """
        self.close_current_menu()
        gesamt_ipt_druck_frame = tk.Frame(self)
        gesamt_ipt_druck_frame.pack(padx=10, pady=10)
        self.current_menu_frame = gesamt_ipt_druck_frame

        # Konfiguration für 7 Tage
        config_7_days = {
            'device_id': alledrei,
            'days': 7,
            'x_label': 'Zeit',
            'y_label': 'Druck',
            'title': 'Druckverlauf letzte 7 Tage',
            'x_key': 'zeitstempel',
            'y_key': 'druck'
        }
        tk.Button(
            gesamt_ipt_druck_frame,
            text="7 Tage",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_7_days),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Konfiguration für 24 Stunden
        config_24_hours = {
            'device_id': alledrei,
            'days': 1,
            'x_label': 'Zeit',
            'y_label': 'Druck',
            'title': 'Druckverlauf letzte 24 Stunden',
            'x_key': 'zeitstempel',
            'y_key': 'druck'
        }
        tk.Button(
            gesamt_ipt_druck_frame,
            text="24h",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_24_hours),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            gesamt_ipt_druck_frame, text="Zurück", command=self.close_current_menu
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_gesamt_durchfluss(self):
        """
        Stellt die Benutzeroberfläche für die Durchflussansicht des Kompressors bereit.
        Ermöglicht Benutzern, Durchflussdaten für unterschiedliche Zeiträume zu
        betrachten und zu analysieren.
        """
        self.close_current_menu()
        gesamt_ipt_durchfluss_frame = tk.Frame(self)
        gesamt_ipt_durchfluss_frame.pack(padx=10, pady=10)
        self.current_menu_frame = gesamt_ipt_durchfluss_frame

        # Konfiguration für 7 Tage
        config_7_days = {
            'device_id': alledrei,
            'days': 7,
            'x_label': 'Zeit',
            'y_label': 'Durchfluss',
            'title': 'Durchflussverlauf letzte 7 Tage',
            'x_key': 'zeitstempel',
            'y_key': 'durchfluss'
        }
        tk.Button(
            gesamt_ipt_durchfluss_frame,
            text="7 Tage",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_7_days),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Konfiguration für 24 Stunden
        config_24_hours = {
            'device_id': alledrei,
            'days': 1,
            'x_label': 'Zeit',
            'y_label': 'Durchfluss',
            'title': 'Durchfluss letzte 24 Stunden',
            'x_key': 'zeitstempel',
            'y_key': 'durchfluss'
        }
        tk.Button(
            gesamt_ipt_durchfluss_frame,
            text="24h",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_24_hours),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            gesamt_ipt_durchfluss_frame, text="Zurück", command=self.close_current_menu
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_gesamt_temperatur(self):
        """
        Öffnet die Ansicht für die Temperaturdaten des Kompressors.
        Benutzer können Temperaturverläufe für verschiedene Zeiträume auswählen und anzeigen.
        """
        self.close_current_menu()
        gesamt_ipt_temperatur_frame = tk.Frame(self)
        gesamt_ipt_temperatur_frame.pack(padx=10, pady=10)
        self.current_menu_frame = gesamt_ipt_temperatur_frame

        # Konfiguration für 7 Tage
        config_7_days = {
            'device_id': alledrei,
            'days': 7,
            'x_label': 'Zeit',
            'y_label': 'Temperatur',
            'title': 'Temperaturverlauf letzte 7 Tage',
            'x_key': 'zeitstempel',
            'y_key': 'temperatur'
        }
        tk.Button(
            gesamt_ipt_temperatur_frame,
            text="7 Tage",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_7_days),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Konfiguration für 24 Stunden
        config_24_hours = {
            'device_id': alledrei,
            'days': 1,
            'x_label': 'Zeit',
            'y_label': 'Temperatur',
            'title': 'Temperaturverlauf letzte 24 Stunden',
            'x_key': 'zeitstempel',
            'y_key': 'temperatur'
        }
        tk.Button(
            gesamt_ipt_temperatur_frame,
            text="24h",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_24_hours),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            gesamt_ipt_temperatur_frame, text="Zurück", command=self.close_current_menu
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_gesamt_energie(self):
        """
        Präsentiert die Benutzeroberfläche für die Gesamtenergieansicht des Kompressors.
        Bietet Optionen zur Anzeige von Energieverbrauchsdaten über ausgewählte Zeiträume.
        """
        self.close_current_menu()
        gesamt_ipt_energie_frame = tk.Frame(self)
        gesamt_ipt_energie_frame.pack(padx=10, pady=10)
        self.current_menu_frame = gesamt_ipt_energie_frame

        # Konfiguration für 7 Tage
        config_7_days = {
            'device_id': alledrei,
            'days': 7,
            'x_label': 'Zeit',
            'y_label': 'Energie',
            'title': 'Energieverlauf letzte 7 Tage',
            'x_key': 'zeitstempel',
            'y_key': 'energie'
        }
        tk.Button(
            gesamt_ipt_energie_frame,
            text="7 Tage",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_7_days),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Konfiguration für 24 Stunden
        config_24_hours = {
            'device_id': alledrei,
            'days': 1,
            'x_label': 'Zeit',
            'y_label': 'Energie',
            'title': 'Energieverlauf letzte 24 Stunden',
            'x_key': 'zeitstempel',
            'y_key': 'energie'
        }
        tk.Button(
            gesamt_ipt_energie_frame,
            text="24h",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_24_hours),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            gesamt_ipt_energie_frame, text="Zurück", command=self.close_current_menu
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_historische_daten_druck(self):
        """
        Zeigt die Benutzeroberfläche für historische Daten des Kompressors Ostfalia.
        """
        self.close_current_menu()
        historische_daten_druck_frame = tk.Frame(self)
        historische_daten_druck_frame.pack(padx=10, pady=10)
        self.current_menu_frame = historische_daten_druck_frame

        # Konfiguration für die Anzeige der historischen Druckdaten
        config_historische_daten = {
            'device_id': alledrei,
            'days': '',
            'x_label': 'Zeit',
            'y_label': 'Druck',
            'title': 'Historischer Druckverlauf',
            'x_key': 'zeitstempel',
            'y_key': 'druck'
        }
        tk.Button(
            historische_daten_druck_frame,
            text="Druck",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_historische_daten),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(
            historische_daten_druck_frame,
            text="Zurück",
            command=self.close_current_menu,
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_historische_daten_durchfluss(self):
        """
        Bietet eine Ansicht der historischen Durchflussdaten des Kompressors.
        Ermöglicht detaillierte Analysen des Durchflussverhaltens über die Zeit.
        """
        self.close_current_menu()
        historische_daten_durchfluss_frame = tk.Frame(self)
        historische_daten_durchfluss_frame.pack(padx=10, pady=10)
        self.current_menu_frame = historische_daten_durchfluss_frame

        # Konfiguration für die Anzeige der historischen Durchflussdaten
        config_historische_daten = {
            'device_id': alledrei,
            'days': '',
            'x_label': 'Zeit',
            'y_label': 'Durchfluss',
            'title': 'Historischer Durchflussverlauf',
            'x_key': 'zeitstempel',
            'y_key': 'durchfluss'
        }
        tk.Button(
            historische_daten_durchfluss_frame,
            text="Durchfluss",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_historische_daten),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(
            historische_daten_durchfluss_frame,
            text="Zurück",
            command=self.close_current_menu,
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_historische_daten_temperatur(self):
        """
        Stellt die historischen Temperaturdaten des Kompressors dar.
        Ermöglicht es Benutzern, Temperaturtrends über längere Zeiträume zu verfolgen.
        """
        self.close_current_menu()
        historische_daten_temperatur_frame = tk.Frame(self)
        historische_daten_temperatur_frame.pack(padx=10, pady=10)
        self.current_menu_frame = historische_daten_temperatur_frame

        # Konfiguration für die Anzeige der historischen Temperaturdaten
        config_historische_daten = {
            'device_id': alledrei,
            'days': '',
            'x_label': 'Zeit',
            'y_label': 'Temperatur',
            'title': 'Historischer Temperaturverlauf',
            'x_key': 'zeitstempel',
            'y_key': 'temperatur'
        }
        tk.Button(
            historische_daten_temperatur_frame,
            text="Temperatur",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_historische_daten),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(
            historische_daten_temperatur_frame,
            text="Zurück",
            command=self.close_current_menu,
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_historische_daten_energie(self):
        """
        Zeigt die historischen Energieverbrauchsdaten des Kompressors.
        Bietet Einblicke in den Energieverbrauch des Kompressors über verschiedene Zeiträume.
        """
        self.close_current_menu()
        historische_daten_energie_frame = tk.Frame(self)
        historische_daten_energie_frame.pack(padx=10, pady=10)
        self.current_menu_frame = historische_daten_energie_frame

        # Konfiguration für die Anzeige der historischen Energieverbrauchsdaten
        config_historische_daten = {
            'device_id': alledrei,
            'days': '',
            'x_label': 'Zeit',
            'y_label': 'Energie',
            'title': 'Historischer Energieverlauf',
            'x_key': 'zeitstempel',
            'y_key': 'energie'
        }
        tk.Button(
            historische_daten_energie_frame,
            text="Energie",
            command=lambda: self.filter_and_plot_data(daten_komplett, config_historische_daten),
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(
            historische_daten_energie_frame,
            text="Zurück",
            command=self.close_current_menu,
        ).pack(pady=5, padx=10, side=tk.LEFT)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
