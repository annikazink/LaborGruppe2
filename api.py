import requests
import pymysql
import sys
import traceback
import time
import smtplib
from email.mime.text import MIMEText

class Api:
    relevant_keys = {
        "Kompressor_IPT": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],
        "Kompressor_IPT_Entlueftung": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],
        "Kompressor_IPT_Kuehler": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],
        "Kompressor_IPT_Sensoren": ["ID", "Zeitstempel", "Druck", "Durchfluss", "Temperatur1"],
        "Kompressor_Ostfalia": ["ID", "Zeitstempel", "Energie_gesamt_kwh"],
    }

    def log_error(self, error_message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open('error_log.txt', 'a') as f:
            f.write(f"{timestamp} - {error_message}\n")

        self.send_email("Error Notification: Kompressor Datenbank", f"Error occurred: {error_message}")

    def send_email(self, subject, body):
        # Set up email server
        smtp_server = 'smtp.gmail.com'
        port = 587
        sender_email = "mxmkzk03@gmail.com" #infodreilaborwinter2023
        receiver_email = 'm.kozik@ostfalia.de'
        app_password = "omoi gpqv pmhc rghu" #xX_Info.Labor!Winter#2023*

        # Compose the email
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

    def get_response_url(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                error_message = f"Fehlerhafte Abfrage. Status Code: {response.status_code}"
                self.log_error(error_message)
                return None
        except Exception as e:
            error_message = f"Error in get_response_url: {str(e)}"
            self.log_error(error_message)
            return None

    def get_relevant_data(self, api_response, relevant_keys):
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
            error_message = f"Error in get_relevant_data: {str(e)}"
            self.log_error(error_message)
            return None

    def connect_to_database(self):
        try:
            connection = pymysql.connect(host='141.41.42.211',
                                         user='Kompressor',
                                         password='Kompressor12345%',
                                         database='kompressor',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
            return connection
        except pymysql.Error as e:
            error_message = f"Error connecting to the database: {e}"
            self.log_error(error_message)
            return None

    def insert_test_data(self):
        connection = self.connect_to_database()
        try:
            with connection.cursor() as cursor:
                test_data = {
                    "ID_Geraet": 0,
                    "Bereich": "Test",
                    "Zeitstempel": "2023-01-01 12:00:00",
                    "Energie": 1000,
                    "Sensor": 0,
                }
                sql = "INSERT INTO geraet (gerät_id, bereich, zeitstempel, energie, sensor_id) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (
                test_data["ID_Geraet"], test_data["Bereich"], test_data["Zeitstempel"], test_data["Energie"],
                test_data["Sensor"]))
            connection.commit()
        except pymysql.Error as e:
            error_message = f"Error inserting test data into the database: {e}"
            self.log_error(error_message)
        finally:
            connection.close()

    def delete_test_data(self):
        connection = self.connect_to_database()
        if connection:
            try:
                with connection.cursor() as cursor:
                    sql = "DELETE FROM geraet WHERE gerät_id = %s"
                    cursor.execute(sql, 0)
                connection.commit()
            except pymysql.Error as e:
                error_message = f"Error deleting test data from the database: {e}"
                self.log_error(error_message)
            finally:
                connection.close()

    def insert_data(self, relevant_data):
        connection = self.connect_to_database()
        if connection:
            try:
                with connection.cursor() as cursor:
                    for category, entries in relevant_data.items():
                        for entry in entries:
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
                                sql = "INSERT INTO geraet (datag_id, bereich, zeitstempel, energie, geraet_id, datas_id) VALUES (%s, %s, %s, %s, %s, %s)"
                                cursor.execute(sql, (
                                    entry["ID"],
                                    category,
                                    entry["Zeitstempel"],
                                    entry["Energie_gesamt_kwh"],
                                    self.get_geraete_id(category),
                                    relevant_data["Kompressor_IPT_Sensoren"][0]["ID"]
                                ))
                            else:
                                sql = "INSERT INTO geraet (datag_id, bereich, zeitstempel, energie, geraet_id) VALUES (%s, %s, %s, %s, %s)"
                                cursor.execute(sql, (
                                    entry["ID"],
                                    category,
                                    entry["Zeitstempel"],
                                    entry["Energie_gesamt_kwh"],
                                    self.get_geraete_id(category)
                                ))
                connection.commit()
            except pymysql.Error as e:
                error_message = f"Error inserting data into the database: {e}"
                self.log_error(error_message)
            finally:
                connection.close()

    def get_geraete_id(self, category):
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
        try:
            url = "http://141.41.235.28/JSON_Kompressor_IPT/Kompressor_Json.php"
            api_response = self.get_response_url(url)
            relevant_data = self.get_relevant_data(api_response, self.relevant_keys)
            self.insert_data(relevant_data)
        except Exception as e:
            error_message = f"Error in main: {str(e)}"
            self.log_error(error_message)
            sys.exit(1)

if __name__ == '__main__':
    api_instance = Api()
    api_instance.main()



