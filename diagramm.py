"""
Klasse zur erstellung von Diagrammen
"""
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib import dates as mdates


def filter_data_by_period(data_array, days):
    """
    Filtert die Daten, um nur die Einträge der letzten angegebenen Tage zurückzugeben.
    """

    current_time = datetime.now()
    threshold_time = current_time - timedelta(days=days)
    return [
        record
        for record in data_array
        if datetime.strptime(record["zeitstempel"], "%Y-%m-%d %H:%M:%S")
        > threshold_time
    ]


def filter_data_by_device_id(data_array, device_id):
    """
    Filtert die Daten basierend auf der angegebenen Geräte-ID.
    """

    return [record for record in data_array if record["geraet_id"] == device_id]


def plot_data(
    data_array,
    x_label="X-Achse",
    y_label="Y-Achse",
    title="Diagramm",
    x_key="zeitstempel",
    y_key="",
):
    """
    Erstellt ein Diagramm aus den bereitgestellten Daten, wobei Beschriftungen
    und Titel angepasst werden können.
    """
    data_array.sort(key=lambda x: datetime.strptime(x[x_key], "%Y-%m-%d %H:%M:%S"))
    x_data = [
        datetime.strptime(record[x_key], "%Y-%m-%d %H:%M:%S") for record in data_array
    ]
    y_data = [record[y_key] for record in data_array]

    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, marker="o", linestyle="-", color="b")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    axis = plt.gca()
    axis.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%Y\n%H:%M"))
    axis.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.grid()
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.show()


def filter_and_plot_data(data_array, config):
    """
    Kombiniert das Filtern der Daten nach Geräte-ID und Zeitraum
     mit der Erstellung eines Diagramms.
    """
    device_id = config.get("device_id")
    days = config.get("days")
    x_label = config.get("x_label", "")
    y_label = config.get("y_label", "")
    title = config.get("title", "")
    x_key = config.get("x_key", "zeitstempel")
    y_key = config.get("y_key", "")

    filtered_data = filter_data_by_device_id(data_array, device_id)
    filtered_data = filter_data_by_period(filtered_data, days)
    plot_data(filtered_data, x_label, y_label, title, x_key, y_key)


def filter_and_plot_historische_daten(data_array, config):
    """
    Kombiniert das Filtern der Daten nach Geräte-ID und Zeitraum
    mit der Erstellung eines Diagramms.
    """
    device_id = config.get("device_id")
    x_label = config.get("x_label", "Zeit")
    y_label = config.get("y_label", "Wert")
    title = config.get("title", "Diagramm")
    x_key = config.get("x_key", "zeitstempel")
    y_key = config.get("y_key", "")

    # Filtern der Daten basierend auf der Geräte-ID
    filtered_data = [
        record for record in data_array if record.get("geraet_id") == device_id
    ]

    # Daten sortieren nach Zeitstempel
    filtered_data.sort(
        key=lambda x: datetime.strptime(x.get(x_key, ""), "%Y-%m-%d %H:%M:%S")
    )

    # Extrahieren von X- und Y-Daten
    x_data = [
        datetime.strptime(record.get(x_key, ""), "%Y-%m-%d %H:%M:%S")
        for record in filtered_data
    ]
    y_data = [record.get(y_key, 0) for record in filtered_data]

    # Diagramm erstellen
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, marker="o", linestyle="-", color="b")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Anpassung der X-Achse
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    plt.gca().xaxis.set_major_locator(
        mdates.DayLocator(interval=1)
    )  # Jeden Tag markieren
    plt.xticks(rotation=45)

    plt.grid()
    plt.tight_layout()
    plt.show()


def plot_gesamt_energie(gesamt_energie_daten, days):
    """
    Plottet die Gesamtenergie über die angegebenen Tage.

    Diese Methode nimmt Energieverbrauchsdaten und eine Zeitspanne in Tagen entgegen,
     filtert die Daten
    für den angegebenen Zeitraum und erstellt einen Plot,
     der den Gesamtenergieverlauf über diesen Zeitraum zeigt.

    """

    filtered_data = filter_data_by_period(gesamt_energie_daten, days)

    # Extrahiere Zeitstempel und gesamt_energie aus den Datensätzen
    zeitstempel = [
        datetime.strptime(datensatz["zeitstempel"], "%Y-%m-%d %H:%M:%S")
        for datensatz in filtered_data
    ]
    gesamt_energie = [datensatz["gesamt_energie"] for datensatz in filtered_data]

    # Plot erstellen
    plt.figure(figsize=(10, 5))
    plt.plot(zeitstempel, gesamt_energie, marker="o", linestyle="-")
    plt.title("Gesamtenergieverlauf")
    plt.xlabel("Zeitstempel")
    plt.ylabel("Gesamtenergie")

    # Anpassung der X-Achse
    plt.gca().xaxis.set_major_formatter(
        plt.matplotlib.dates.DateFormatter("%Y-%m-%d\n%H:%M")
    )  # Formatierung der Zeitstempel
    # Intervall der Zeitstempel
    plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.DayLocator(interval=1))
    plt.xticks(rotation=45)  # Rotation der Zeitstempel

    plt.grid(True)
    plt.tight_layout()  # Sorgt für eine ordentliche Anordnung der Plot-Elemente
    plt.show()
