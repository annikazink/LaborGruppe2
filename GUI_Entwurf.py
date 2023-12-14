import matplotlib.pyplot as plt
import random


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.attributes('-fullscreen', True)  # Starte im Vollbildmodus
        self.attributes("-fullscreen", True)  # Starte im Vollbildmodus

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
@@ -19,7 +20,9 @@ def __init__(self):
        self.notebook.add(kompressor_ostfalia_frame, text="Kompressor Ostfalia")

        # Füge den Schließen-Button hinzu
        close_button = tk.Button(self, text="X", command=self.quit, font=("Arial", 12), width=2, height=1)
        close_button = tk.Button(
            self, text="X", command=self.quit, font=("Arial", 12), width=2, height=1
        )
        close_button.place(relx=1, rely=0, anchor=tk.NE)

        self.create_kompressor_ipt_buttons(kompressor_ipt_frame)
@@ -32,9 +35,15 @@ def __init__(self):
        # Labels für die Sensorwerte
        self.sensor_labels = {
            "Druck": tk.Label(self.sensor_status_frame, text="", font=("Arial", 12)),
            "Durchfluss": tk.Label(self.sensor_status_frame, text="", font=("Arial", 12)),
            "Temperatur 1": tk.Label(self.sensor_status_frame, text="", font=("Arial", 12)),
            "Temperatur 2": tk.Label(self.sensor_status_frame, text="", font=("Arial", 12))
            "Durchfluss": tk.Label(
                self.sensor_status_frame, text="", font=("Arial", 12)
            ),
            "Temperatur 1": tk.Label(
                self.sensor_status_frame, text="", font=("Arial", 12)
            ),
            "Temperatur 2": tk.Label(
                self.sensor_status_frame, text="", font=("Arial", 12)
            ),
        }

        # Platzierung der Sensorlabels
@@ -49,21 +58,21 @@ def show_sensor_status():
                "Druck": "100 PSI",
                "Durchfluss": "50 L/min",
                "Temperatur 1": "25°C",
                "Temperatur 2": "30°C"
                "Temperatur 2": "30°C",
            }

            # Zeige die Sensordaten in Labels an
            for key, value in sensor_data.items():
                self.sensor_labels[key]["text"] = f"{key}: {value}"

        def show_temperature():
            zeit = range(0,25)
            zeit = range(0, 25)
            temperatur = [random.uniform(18, 30) for _ in range(25)]
            plt.figure(figsize=(10, 6))
            plt.plot(zeit, temperatur, marker='o', linestyle='-', color='b')
            plt.title('Temperatur über 24 Stunden')
            plt.xlabel('Zeit (Stunden)')
            plt.ylabel('Temperatur (°C)')
            plt.plot(zeit, temperatur, marker="o", linestyle="-", color="b")
            plt.title("Temperatur über 24 Stunden")
            plt.xlabel("Zeit (Stunden)")
            plt.ylabel("Temperatur (°C)")
            plt.grid(True)
            plt.show()

@@ -72,20 +81,69 @@ def reset_sensor_status():
            for key in self.sensor_labels:
                self.sensor_labels[key]["text"] = ""

        tk.Button(frame, text="Energieverbrauch", font=("Arial", 12), width=20, height=3, command=reset_sensor_status).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(frame, text="Temperaturen", font=("Arial", 12), width=20, height=3, command=reset_sensor_status).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(frame, text="Messwerte", font=("Arial", 12), width=20, height=3, command=reset_sensor_status).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(frame, text="Systemdruck", font=("Arial", 12), width=20, height=3, command=reset_sensor_status).grid(row=0, column=3, padx=10, pady=5)
        tk.Button(frame, text="Historische Daten", font=("Arial", 12), width=20, height=3, command=reset_sensor_status).grid(row=0, column=4, padx=10, pady=5)
        tk.Button(
            frame,
            text="Energieverbrauch",
            font=("Arial", 12),
            width=20,
            height=3,
            command=reset_sensor_status,
        ).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(
            frame,
            text="Temperaturen",
            font=("Arial", 12),
            width=20,
            height=3,
            command=reset_sensor_status,
        ).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(
            frame,
            text="Messwerte",
            font=("Arial", 12),
            width=20,
            height=3,
            command=reset_sensor_status,
        ).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(
            frame,
            text="Systemdruck",
            font=("Arial", 12),
            width=20,
            height=3,
            command=reset_sensor_status,
        ).grid(row=0, column=3, padx=10, pady=5)
        tk.Button(
            frame,
            text="Historische Daten",
            font=("Arial", 12),
            width=20,
            height=3,
            command=reset_sensor_status,
        ).grid(row=0, column=4, padx=10, pady=5)

        # Button "Status Sensoren" neben den anderen Buttons platzieren
        tk.Button(frame, text="Status Sensoren", font=("Arial", 12), width=20, height=3, command=show_sensor_status).grid(row=0, column=5, padx=10, pady=5)
        tk.Button(
            frame,
            text="Status Sensoren",
            font=("Arial", 12),
            width=20,
            height=3,
            command=show_sensor_status,
        ).grid(row=0, column=5, padx=10, pady=5)

    def create_kompressor_ostfalia_buttons(self, frame):
        tk.Button(frame, text="Energieverbräuche", font=("Arial", 12), width=20, height=3).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(frame, text="Messwerte", font=("Arial", 12), width=20, height=3).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(frame, text="Historische Daten", font=("Arial", 12), width=20, height=3).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(
            frame, text="Energieverbräuche", font=("Arial", 12), width=20, height=3
        ).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(frame, text="Messwerte", font=("Arial", 12), width=20, height=3).grid(
            row=0, column=1, padx=10, pady=5
        )
        tk.Button(
            frame, text="Historische Daten", font=("Arial", 12), width=20, height=3
        ).grid(row=0, column=2, padx=10, pady=5)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
    app.mainloop()