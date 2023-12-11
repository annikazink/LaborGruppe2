import requests

comp_url = "http://141.41.235.28/JSON_Kompressor_IPT/Kompressor_Json.php"
def test_api_request_successful():
    response = requests.get(comp_url)
    assert response.status_code == 200

def test_api_request_returns_json():
    response = requests.get(comp_url)
    assert response.headers['Content-Type'] == 'application/json'

#def test_get_relevant_data():
