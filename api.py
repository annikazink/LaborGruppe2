'''
Informatik III Labor WS23/24: Kompressordaten

API-Kommunikation und Datenbankintegration

Dieses Skript dient der Kommunikation mit einer externen API, die die Daten eines Kompressors enthält,
der Verarbeitung relevanter Daten und der Integration in eine MySQL-Datenbank.

Author: Hannes Kamann 70481032
        Maxim Kozik 70481254

'''

import requests
import pymysql
import sys
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime


class Api:
    # Relevanten Schlüssel für die Datenextraktion aus der API-Response
    relevant_keys = {
        "Kompressor_IPT": ["Zeitstempel", "Energie_gesamt_kwh"],
        "Kompressor_IPT_Entlueftung": ["Zeitstempel", "Energie_gesamt_kwh"],
        "Kompressor_IPT_Kuehler": ["Zeitstempel", "Energie_gesamt_kwh"],
        "Kompressor_IPT_Sensoren": ["ID", "Zeitstempel", "Druck", "Durchfluss", "Temperatur1"],
        "Kompressor_Ostfalia": ["Zeitstempel", "Energie_gesamt_kwh"],
    }

    def __init__(self):
        if not hasattr(Api, 'start_time'):
            Api.start_time = time.time()
    def log_error(self, error_message):
        '''
        Loggt Fehlermeldungen in eine Datei und sendet eine Benachrichtigung per E-Mail.

        :param error_message: Die Fehlermeldung
        '''
        sendingMail = False
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open('error_log.txt', 'a') as f:
            f.write(f"{timestamp} - {error_message}\n")
        if sendingMail:
            self.send_email("Fehlerbenachrichtigung: Kompressor Datenbank", f"Fehler aufgetreten: {error_message}")

    def send_email(self, subject, body):
        '''
        Versendet eine E-Mail-Benachrichtigung über einen SMTP-Server.

        :param subject: Der Betreff der E-Mail
        :param body: Der Inhalt der E-Mail
        '''
        # E-Mail Serverkonfiguration
        smtp_server = 'smtp.gmail.com'
        port = 587
        sender_email = "infodreilaborwinter2023@gmail.com"  # [Deine E-Mail-Adresse]
        receiver_email = 'm.kozik@ostfalia.de'
        app_password = "iqon snvs vmtd wabb"  # [Dein E-Mail-App-Passwort]

        # E-Mail erstellen
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        # Mit dem SMTP-Server verbinden und die E-Mail senden
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())



    def get_response_url(self, url):
        '''
        Holt die API-Antwort von der angegebenen URL.

        :param url: Die URL der API
        :return: Die JSON-antwort der API oder None bei einem Fehler
        '''
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                error_message = f"Fehlerhafte Abfrage. Status Code: {response.status_code}"
                self.log_error(error_message)
                return None
        except Exception as e:
            error_message = f"Fehler in get_response_url: {str(e)}"
            self.log_error(error_message)
            return None

    def get_relevant_data(self, api_response, relevant_keys):
        '''
        Extrahiert die relevanten Daten aus der API-Antwort.

        :param api_response: Die API-Antwort im JSON-Format
        :param relevant_keys: Die Schlüssel für relevante Daten
        :return: Ein Dictionary mit den relevanten Daten oder None bei einem Fehler
        '''
        try:
            relevant_data = {}
            for category, keys in relevant_keys.items():
                if category in api_response:
                    relevant_data[category] = []
                    for entry in api_response[category]:
                        relevant_entry = {}
                        for key in keys:
                            relevant_entry[key] = entry.get(key)
                        relevant_data[category].append(relevant_entry)
            return relevant_data
        except Exception as e:
            error_message = f"Fehler in get_relevant_data: {str(e)}"
            self.log_error(error_message)
            return None

    def connect_to_database(self):
        '''
        Stellt eine Verbindung zur MySQL-Datenbank her.

        :return: Die Verbindungsinstanz zur Datenbank oder None bei einem Fehler
        '''
        try:
            connection = pymysql.connect(host='141.41.42.211',
                                         user='Kompressor',
                                         password='Kompressor12345%',
                                         database='kompressor',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
            return connection
        except pymysql.Error as e:
            error_message = f"Fehler beim Verbinden mit der Datenbank: {e}"
            self.log_error(error_message)
            return None

    def insert_data(self, relevant_data):
        '''
        Fügt relevante Daten in die Datenbank ein.

        :param relevant_data: Ein Dictionary mit den relevanten Daten
        '''
        connection = self.connect_to_database()
        if connection:
            try:
                with connection.cursor() as cursor:
                    for category, entries in relevant_data.items():
                        for entry in entries:
                            try:
                                if category == "Kompressor_IPT_Sensoren":
                                    sql = "INSERT INTO sensor (datas_id, zeitstempel, druck, durchfluss, temperatur, sensor_id) VALUES (%s, %s, %s, %s, %s, %s)"
                                    cursor.execute(sql, (
                                        entry["ID"],
                                        entry["Zeitstempel"],
                                        entry["Druck"],
                                        entry["Durchfluss"],
                                        entry["Temperatur1"],
                                        1
                                    ))
                                elif category == "Kompressor_IPT":
                                    sql = "INSERT INTO geraet (bereich, zeitstempel, energie, geraet_id, datas_id) VALUES (%s, %s, %s, %s, %s)"
                                    cursor.execute(sql, (
                                        category,
                                        entry["Zeitstempel"],
                                        entry["Energie_gesamt_kwh"],
                                        self.get_geraete_id(category),
                                        relevant_data["Kompressor_IPT_Sensoren"][0]["ID"]
                                    ))
                                else:
                                    sql = "INSERT INTO geraet (bereich, zeitstempel, energie, geraet_id) VALUES (%s, %s, %s, %s)"
                                    cursor.execute(sql, (
                                        category,
                                        entry["Zeitstempel"],
                                        entry["Energie_gesamt_kwh"],
                                        self.get_geraete_id(category)
                                    ))
                                connection.commit()

                            except pymysql.IntegrityError as integrity_error:
                                erfolg = False
                                # Bei einem Duplikateintrag Fehler protokollieren
                                duplicate_error_message = f"Duplicate Entry Error: {integrity_error}. Gerät: {category}, Daten-ID: {entry['ID']}, Zeitstempel: {entry['Zeitstempel']}"

                                # existing_entry enthalten alle Informationen über den vorhandenen Eintrag
                                existing_entry_sql = f"SELECT * FROM geraet WHERE datag_id = {entry['ID']}"
                                cursor.execute(existing_entry_sql)
                                existing_entry = cursor.fetchone()

                                if existing_entry:
                                    # Zeitstempel in lesbares Format konvertieren
                                    existing_entry_zeitstempel = existing_entry['zeitstempel'].strftime(
                                        "%Y-%m-%d %H:%M:%S")
                                    duplicate_error_message += f"\nBereits vorhandener Eintrag: {existing_entry_zeitstempel}, {existing_entry}\n"

                                self.log_error(duplicate_error_message)
            except pymysql.Error as e:
                erfolg = False
                error_message = f"Fehler beim Einfügen von Daten in die Datenbank: {e}"
                self.log_error(error_message)
            finally:
                connection.close()

    def get_geraete_id(self, category):
        '''
        Gibt die Geräte-ID basierend auf der Kategorie zurück.

        :param category: Die Kategorie des Geräts
        :return: Die Geräte-ID oder None bei unbekannter Kategorie
        '''
        if category == "Kompressor_IPT":
            return 1
        elif category == "Kompressor_IPT_Entlueftung":
            return 2
        elif category == "Kompressor_IPT_Kuehler":
            return 3
        elif category == "Kompressor_Ostfalia":
            return 4
        else:
            return None

    def main(self):
        '''
        Hauptfunktion des Skripts, die die API-Antwort abruft, relevante Daten extrahiert und in die Datenbank einfügt.
        '''
        try:
            url = "http://141.41.235.28/JSON_Kompressor_IPT/Kompressor_Json.php"
            api_response = self.get_response_url(url)
            relevant_data = self.get_relevant_data(api_response, self.relevant_keys)
            self.insert_data(relevant_data)

        except Exception as e:
            error_message = f"Fehler in main: {str(e)}"
            self.log_error(error_message)
            sys.exit(1)

if __name__ == '__main__':
    api_instance = Api()
    api_instance.main()
