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

# Verbindung zur Datenbank herstellen
connection = connect_to_database()

if connection:
    print("Verbindung zur Datenbank hergestellt.")
    # Hier kannst du Datenbankabfragen ausführen oder andere Operationen durchführen
    # Vergiss nicht, die Verbindung am Ende zu schließen: connection.close()
else:
    print("Keine Verbindung zur Datenbank hergestellt.")

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

# Tabellennamen abrufen und anzeigen
tables = get_table_names()
if tables:
    print("Verfügbare Tabellen:")
    for table in tables:
        print(table)

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
# Funktion, die aufgerufen wird, wenn der "Historie" -Button geklickt wird

# Funktion, die aufgerufen wird, wenn der "Historie" -Button geklickt wird
# Funktion, die aufgerufen wird, wenn der "Historie" -Button geklickt wird
def on_historie_button_click():
    last_10_records = get_last_10_records("geraet")  # Ersetze 'deine_tabelle' durch den tatsächlichen Tabellennamen
    if last_10_records:
        historie_text.delete(1.0, tk.END)  # Lösche den aktuellen Inhalt des Textfelds
        for record in last_10_records:
            formatted_record = f"ID: Energie: {record['energie']}, Zeitstempel: {record['zeit']}\n"
            historie_text.insert(tk.END, formatted_record)  # Füge jeden Datensatz im gewünschten Format in das Textfeld ein

# Erstelle ein tkinter-Fenster
root = tk.Tk()
root.title("Historie")

# Erstelle den "Historie" -Button
historie_button = tk.Button(root, text="Historie", command=on_historie_button_click)
historie_button.pack()

# Erstelle ein Textfeld zur Anzeige der Historie
historie_text = tk.Text(root, height=10, width=50)
historie_text.pack()

# Starte die tkinter-Hauptloop
root.mainloop()