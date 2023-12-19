# Verbindung zur Datenbank
# funktioniert noch nicht

import pymysql
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

def connect_to_database():
    try:
        connection = pymysql.connect(
            host='141.41.42.211',
            user='Kompressor',
            password='Kompressor12345%',
            database='kompressor',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        return connection
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def get_table_names():
    connection = connect_to_database()
    if connection:
        try:
            # Tabellennamen abrufen
            with connection.cursor() as cursor:
                sql = "SHOW TABLES"
                cursor.execute(sql)
                tables = cursor.fetchall()
                table_names = [table_value for table_dict in tables for table_value in table_dict.values()]
                return table_names

        except pymysql.Error as e:
            print(f"Fehler beim Ausführen der SQL-Abfrage: {e}")

        finally:
            connection.close()  # Verbindung schließen, wenn fertig
    else:
        print("Keine Verbindung zur Datenbank hergestellt.")

# Funktion zum Abrufen der letzten 10 Datensätze der energie der geraet Tabelle
def get_last_10_records(table_name):
    connection = connect_to_database()
    if connection:
        try:
            # Die letzten 10 Datensätze abrufen
            with connection.cursor() as cursor:
                sql = f"SELECT * FROM {table_name} ORDER BY energie DESC LIMIT 10"  # Ersetze 'id' durch die tatsächliche Primärschlüsselspalte
                cursor.execute(sql)
                records = cursor.fetchall()
                return records

        except pymysql.Error as e:
            print(f"Fehler beim Ausführen der SQL-Abfrage: {e}")

        finally:
            connection.close()  # Verbindung schließen, wenn fertig
    else:
        print("Keine Verbindung zur Datenbank hergestellt.")

# Folgende Funktion ruft die Energiewerte für den Kompressor IPT ab.
def on_historie_button_clickOstfalia():
    last_10_records = get_last_10_records("geraet")  # Ersetze 'deine_tabelle' durch den tatsächlichen Tabellennamen
    if last_10_records:
        historie_text.delete(1.0, tk.END)  # Lösche den aktuellen Inhalt des Textfelds
        for record in last_10_records:
            formatted_record = f"ID: {record['geraet_id']}, Energie: {record['energie']}, Zeitstempel: {record['zeitstempel']}\n"
            historie_text.insert(tk.END, formatted_record)  # Füge jeden Datensatz im gewünschten Format in das Textfeld ein

# Folgende Funktion ruft druck, durchfluss, temperaturwerte des Kompressor Ostfalia ab
def on_historie_button_clickIPT():
    last_10_records = get_last_10_records("sensor")  # Ersetze 'deine_tabelle' durch den tatsächlichen Tabellennamen
    if last_10_records:
        historie_text.delete(1.0, tk.END)  # Lösche den aktuellen Inhalt des Textfelds
        for record in last_10_records:
            formatted_record = f"ID: {record['geraet_id']}, Druck: {record['druck']}, Durchfluss: {record['durchfluss']}, temperatur: {record['temperatur']}, Zeitstempel: {record['zeitstempel']}\n"
            historie_text.insert(tk.END, formatted_record)  # Füge jeden Datensatz im gewünschten Format in das Textfeld ein

# Erstelle ein tkinter-Fenster
root = tk.Tk()
root.title("Historie")

# Erstelle den "HistorieIPT" -Button
historieIPT_button = tk.Button(root, text="Historie IPT", command=on_historie_button_clickIPT)
historieIPT_button.pack()

historieOstfalia_button = tk.Button(root, text='Historie Ostfalia', command=on_historie_button_clickOstfalia)
historieOstfalia_button.pack()

# Erstelle ein Textfeld zur Anzeige der Historie
historie_text = tk.Text(root, height=50, width=60)
historie_text.pack()

# Starte die tkinter-Hauptloop
root.mainloop()