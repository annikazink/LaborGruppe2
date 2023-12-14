import tkinter as tk
from tkinter import ttk


class MainApp(tk.Tk):
    """
    Hauptanwendung für die GUI.
    Diese Klasse erstellt das Hauptfenster der Anwendung mit verschiedenen Seiten
    und Funktionen zur Anzeige
    von Kompressordaten und anderen Informationen.
    """

    def __init__(self):
        """
        Initialisiert das Hauptfenster der Anwendung.
        """
        super().__init__()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(padx=10, pady=10)

        self.menu_frames = {}
        self.current_menu_frame = None  # Aktuell geöffnetes Menü
        self.temperature_submenu = None  # Referenz auf das Untermenü "Temperatur"
        self.temperature_submenu_7days = None  # Referenz auf das Untermenü "7 Tage"

        self.create_kompressor_ipt_page()
        self.create_kompressor_ostfalia_page()

    def create_kompressor_ipt_page(self):
        """
        Erstellt die Seite für Kompressor IPT im Haupt-Notebook.
        """
        kompressor_ipt_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ipt_frame, text="Kompressor IPT")

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
        Erstellt die Seite für Kompressor Ostfalia im Haupt-Notebook.
        """
        kompressor_ostfalia_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ostfalia_frame, text="Kompressor Ostfalia")

        tk.Button(
            kompressor_ostfalia_frame,
            text="Energieverbrauch",
            command=self.show_kompressor_ostfalia_energieverbrauch,
        ).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(
            kompressor_ostfalia_frame,
            text="Messwerte",
            command=self.show_kompressor_ostfalia_messwerte,
        ).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(
            kompressor_ostfalia_frame,
            text="Historische Daten",
            command=self.show_kompressor_ostfalia_historische_daten,
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def close_current_menu(self):
        """
        Schließt das aktuell geöffnete Menü.
        """
        if self.current_menu_frame:
            self.current_menu_frame.destroy()
            self.current_menu_frame = None

    def show_kompressor_ipt_kompressor(self):
        """
        Zeigt die Daten für den Kompressor IPT.
        """
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        kompressordaten_ipt_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        kompressordaten_ipt_frame.pack(
            padx=10, pady=10
        )  # Platziert den Frame im Hauptfenster
        self.menu_frames[
            "KompressordatenIPT"
        ] = kompressordaten_ipt_frame  # Aktualisiert den Frame-Schlüssel im Dictionary
        self.current_menu_frame = (
            kompressordaten_ipt_frame  # Aktualisiert das aktuell geöffnete Menü
        )

        # Label, das anzeigt, dass aktuell keine Daten verfügbar sind
        tk.Button(
            kompressordaten_ipt_frame,
            text="Energie",
            command=self.plot_kompressor_ipt_kompressor_energie,
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(
            kompressordaten_ipt_frame, text="Zurück", command=self.close_current_menu
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_kompressor_ipt_entluefter(self):
        """
        Zeigt die Benutzeroberfläche für den Entlüfter des Kompressors IPT.
        """
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        entluefter_ipt_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        entluefter_ipt_frame.pack(
            padx=10, pady=10
        )  # Platziert den Frame im Hauptfenster
        entluefter_ipt = (
            entluefter_ipt_frame  # Aktualisiert die Variable auf den neuen Frame
        )
        self.current_menu_frame = (
            entluefter_ipt_frame  # Aktualisiert das aktuell geöffnete Menü
        )

        # Label, das anzeigt, dass aktuell keine Daten verfügbar sind
        tk.Button(
            entluefter_ipt,
            text="Energie",
            command=self.plot_kompressor_ipt_entluefter_energie,
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(entluefter_ipt, text="Zurück", command=self.close_current_menu).pack(
            pady=5, padx=10, side=tk.LEFT
        )

    def show_kompressor_ipt_kuehler(self):
        """
        Zeigt die Benutzeroberfläche für den Kühler des Kompressors IPT.
        """
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        kuehler_ipt_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        kuehler_ipt_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        kuehler_ipt = kuehler_ipt_frame  # Aktualisiert die Variable auf den neuen Frame
        self.current_menu_frame = (
            kuehler_ipt_frame  # Aktualisiert das aktuell geöffnete Menü
        )

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(
            kuehler_ipt,
            text="Energie",
            command=self.plot_kompressor_ipt_kuehler_energie,
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(kuehler_ipt, text="Zurück", command=self.close_current_menu).pack(
            pady=5, padx=10, side=tk.LEFT
        )

    def show_kompressor_ipt_gesamt(self):
        """
        Zeigt die Benutzeroberfläche für die Gesamtansicht des Kompressors IPT.
        """
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        gesamt_ipt_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        gesamt_ipt_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        gesamt_ipt = gesamt_ipt_frame  # Aktualisiert die Variable auf den neuen Frame
        self.current_menu_frame = (
            gesamt_ipt_frame  # Aktualisiert das aktuell geöffnete Menü
        )

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(
            gesamt_ipt, text="Druck", command=self.plot_kompressor_ipt_gesamt_druck
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            gesamt_ipt,
            text="Durchfluss",
            command=self.plot_kompressor_ipt_gesamt_durchfluss,
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            gesamt_ipt,
            text="Temperatur",
            command=self.plot_kompressor_ipt_gesamt_temperatur,
        ).pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(
            gesamt_ipt, text="Energie", command=self.plot_kompressor_ipt_gesamt_energie
        ).pack(pady=5, padx=10, side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(gesamt_ipt, text="Zurück", command=self.close_current_menu).pack(
            pady=5, padx=10, side=tk.LEFT
        )

    def show_kompressor_ipt_historische_daten(self):
        """
        Zeigt die Benutzeroberfläche für historische Daten des Kompressors IPT.
        """
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        historische_daten_ipt_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        historische_daten_ipt_frame.pack(
            padx=10, pady=10
        )  # Platziert den Frame im Hauptfenster
        historische_daten_ipt = (
            historische_daten_ipt_frame  # Aktualisiert die Variable auf den neuen Frame
        )
        self.current_menu_frame = (
            historische_daten_ipt_frame  # Aktualisiert das aktuell geöffnete Menü
        )

        # Label, das anzeigt, dass aktuell keine historischen Daten verfügbar sind
        tk.Label(
            historische_daten_ipt, text="Aktuell keine historischen Daten verfügbar."
        ).pack(pady=5, padx=10)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(
            historische_daten_ipt, text="Zurück", command=self.close_current_menu
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_kompressor_ostfalia_energieverbrauch(self):
        """
        Zeigt die Benutzeroberfläche für den Energieverbrauch des Kompressors Ostfalia.
        """
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        energieverbrauch_ostfalia_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        energieverbrauch_ostfalia_frame.pack(
            padx=10, pady=10
        )  # Platziert den Frame im Hauptfenster
        energieverbrauch_ostfalia = energieverbrauch_ostfalia_frame
        self.current_menu_frame = (
            energieverbrauch_ostfalia_frame  # Aktualisiert das aktuell geöffnete Menü
        )

        # Label, das den Energieverbrauch anzeigt
        tk.Label(
            energieverbrauch_ostfalia,
            text="Energieverbrauch: [Hier Energieverbrauch einfügen]",
        ).pack(pady=5, padx=10)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(
            energieverbrauch_ostfalia, text="Zurück", command=self.close_current_menu
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_kompressor_ostfalia_messwerte(self):
        """
        Zeigt die Benutzeroberfläche für die Messwerte des Kompressors Ostfalia.
        """

        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        messwerte_ostfalia_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        messwerte_ostfalia_frame.pack(
            padx=10, pady=10
        )  # Platziert den Frame im Hauptfenster
        messwerte_ostfalia = (
            messwerte_ostfalia_frame  # Aktualisiert die Variable auf den neuen Frame
        )
        self.current_menu_frame = (
            messwerte_ostfalia_frame  # Aktualisiert das aktuell geöffnete Menü
        )

        # Label, das die Messwerte anzeigt
        tk.Label(messwerte_ostfalia, text="Messwerte: [Hier Messwerte einfügen]").pack(
            pady=5, padx=10
        )

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(
            messwerte_ostfalia, text="Zurück", command=self.close_current_menu
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def show_kompressor_ostfalia_historische_daten(self):
        """
        Zeigt die Benutzeroberfläche für historische Daten des Kompressors Ostfalia.
        """
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        historische_daten_ostfalia_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        historische_daten_ostfalia_frame.pack(
            padx=10, pady=10
        )  # Platziert den Frame im Hauptfenster
        self.menu_frames[
            "HistorischeDatenOstfalia"
        ] = historische_daten_ostfalia_frame  # Aktualisiert den Frame-Schlüssel im Dictionary
        self.current_menu_frame = (
            historische_daten_ostfalia_frame  # Aktualisiert das aktuell geöffnete Menü
        )

        # Hier kannst du deine historischen Daten anzeigen, z.B. in einem Text-Widget
        historische_daten_label = tk.Label(
            historische_daten_ostfalia_frame, text="Historische Daten anzeigen:"
        )
        historische_daten_label.pack(pady=5, padx=10)

        historische_daten_text = tk.Text(
            historische_daten_ostfalia_frame, width=40, height=10
        )
        historische_daten_text.pack(pady=5, padx=10)

        historische_daten_text.insert(
            tk.END, "Hier werden die historischen Daten angezeigt."
        )

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(
            historische_daten_ostfalia_frame,
            text="Zurück",
            command=self.close_current_menu,
        ).pack(pady=5, padx=10, side=tk.LEFT)

    def plot_kompressor_ipt_kompressor_energie(self):
        """
        Erstellt und zeigt ein Diagramm für die Energieverbrauchsdaten des Kompressors IPT.
        """

        pass

    def plot_kompressor_ipt_entluefter_energie(self):
        """
        Erstellt und zeigt ein Diagramm für die Energieverbrauchsdaten
        des Entlüfters des Kompressors IPT.
        """

        pass

    def plot_kompressor_ipt_kuehler_energie(self):
        """
        Erstellt und zeigt ein Diagramm für die Energieverbrauchsdaten
         des Kühlers des Kompressors IPT.
        """
        pass

    def plot_kompressor_ipt_gesamt_druck(self):
        """
        Erstellt und zeigt ein Diagramm für die Druckdaten des Gesamtsystems
         des Kompressors IPT.
        """
        pass

    def plot_kompressor_ipt_gesamt_durchfluss(self):
        """
        Erstellt und zeigt ein Diagramm für die Durchflussdaten des Gesamtsystems
         des Kompressors IPT.
        """
        pass

    def plot_kompressor_ipt_gesamt_temperatur(self):
        """
        Erstellt und zeigt ein Diagramm für die Temperaturdaten des Gesamtsystems
         des Kompressors IPT.
        """
        pass

    def plot_kompressor_ipt_gesamt_energie(self):
        """
        Erstellt und zeigt ein Diagramm für die Energieverbrauchsdaten
         des Gesamtsystems des Kompressors IPT.
        """
        pass


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
