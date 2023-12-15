import tkinter as tk
import matplotlib.pyplot as plt
import random
import datetime

def create_temperature_options():
    # Funktion, die aufgerufen wird, wenn der "Temperatur" -Button geklickt wird
    temperature_button.pack_forget()  # Verstecke den "Temperatur" -Button
    text_label.config(text="Wählen Sie die Option aus:")  # Ändere die Beschriftung

    # Erstelle die beiden Optionen (24 Stunden und 7 Tage)
    button_24h.pack()
    button_7d.pack()

def create_temperature_chart(hours):
    # Funktion zur Erstellung des Diagramms basierend auf der ausgewählten Option
    timestamps = []
    temperatures = []

    start_time = datetime.datetime.now() - datetime.timedelta(hours=hours)

    for i in range(hours):
        timestamps.append(start_time + datetime.timedelta(hours=i))
        temperatures.append(random.uniform(18, 30))

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, temperatures, marker='o', linestyle='-')
    plt.xlabel('Zeit')
    plt.ylabel('Temperatur (°C)')
    plt.title(f'{hours} Stunden Temperaturverlauf')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

def create_24h_chart():
    create_temperature_chart(24)

def create_7d_chart():
    create_temperature_chart(24 * 7)

# Erstelle ein tkinter-Fenster
root = tk.Tk()
root.title("Temperaturdiagramm")

text_label = tk.Label(root, text="Klicken Sie auf 'Temperatur' um fortzufahren.")
text_label.pack()

# Erstelle den "Temperatur" -Button
temperature_button = tk.Button(root, text="Temperatur", command=create_temperature_options)
temperature_button.pack()

# Erstelle die Buttons für 24 Stunden und 7 Tage (initial versteckt)
button_24h = tk.Button(root, text="24 Stunden", command=create_24h_chart)
button_7d = tk.Button(root, text="7 Tage", command=create_7d_chart)

# Starte die tkinter-Hauptloop
root.mainloop()
