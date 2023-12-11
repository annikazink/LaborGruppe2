import requests

def test_api_request_successful():
    comp_url = "http://141.41.235.28/JSON_Kompressor_IPT/Kompressor_Json.php"
    response = requests.get(comp_url)
    assert response.status_code == 200

def test_api_request_returns_json():
    comp_url = "http://141.41.235.28/JSON_Kompressor_IPT/Kompressor_Json.php"
    response = requests.get(comp_url)
    assert response.headers['Content-Type'] == 'application/json'

#def test_get_relevant_data():
