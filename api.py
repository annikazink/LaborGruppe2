import requests
import pymysql

comp_url = "http://141.41.235.28/JSON_Kompressor_IPT/Kompressor_Json.php"
response = requests.get(comp_url)
data = response.json()

relevant_keys = {
    "Kompressor_IPT": ["ID", "Zeitstempel", "Strom_gesamt"],
    "Kompressor_IPT_Entlueftung": ["ID", "Zeitstempel", "Strom_gesamt"],
}
def get_relevant_data(api_response, relevant_keys):
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

def convert_strings_to_float(data):
    for category, entries in data.items():
        for entry in entries:
            for key, value in entry.items():
                if isinstance(value, str):
                    try:
                        entry[key] = float(value)
                    except ValueError:
                        pass


relevant_data = get_relevant_data(data, relevant_keys)
print(relevant_data)
convert_strings_to_float(relevant_data)

def turn_data_into_list(relevant_data):
    data_list = []
    for category, data in relevant_data.items():
        for entry in data:
            data_list.append(entry)
    return data_list

def extract_values_into_flat_list(relevant_data):
    """
    Extrahiert die Werte aus dem Dictionary der relevanten Daten und speichert sie in einer flachen Liste.

    :param relevant_data: Ein Dictionary mit relevanten Daten für verschiedene Kategorien.
    :return: Eine flache Liste von Werten.
    """
    flat_list = []

    for data in relevant_data.values():
        for entry in data:
            flat_list.extend(entry.values())

    return flat_list

def connect_to_database():
    connection = pymysql.connect(host='localhost',user='kompressor',password='tsN*r10eLxH-gCgy',database='kompressor')

def insert_data_into_database():
    pass

def close_database_connection():
    pass


for category, entries in relevant_data.items():
    for entry in entries:
        id_value = entry.get('ID')
        id_type = type(id_value)
        print(f"Data type of ID value in {category}: {id_type}")