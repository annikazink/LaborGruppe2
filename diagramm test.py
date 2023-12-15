import tkinter as tk
import matplotlib.pyplot as plt
import random
import datetime

def create_temperature_chart():
    # Hier kommt der Code zur Erstellung des Diagramms
    hours = int(input("Wie viele Stunden?"))
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
    plt.title('24-Stunden-Temperaturverlauf')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

# Erstelle ein tkinter-Fenster
root = tk.Tk()
root.title("Temperaturdiagramm")

# Erstelle einen Button für das Temperaturdiagramm
temperature_button = tk.Button(root, text="Temperatur", command=create_temperature_chart)
temperature_button.pack()

# Starte die tkinter-Hauptloop
root.mainloop()
