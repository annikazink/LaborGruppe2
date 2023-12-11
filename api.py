import requests

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

relevant_data = get_relevant_data(data, relevant_keys)
print(relevant_data)
