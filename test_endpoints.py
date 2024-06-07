import requests

BASE_URL = "http://localhost:8000"

def test_create_asset():
    url = f"{BASE_URL}/assets/"
    payload = {
        "name": "Laptop",
        "type": "Electronics",
        "location": "Headquarters"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Create asset test passed.")
    return response.json()["id"]

def test_get_assets():
    url = f"{BASE_URL}/assets/"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert isinstance(response.json(), list), "Expected a list"
    print("Get assets test passed.")

def test_get_asset(asset_id):
    url = f"{BASE_URL}/assets/{asset_id}"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["id"] == asset_id, f"Expected asset ID {asset_id}, got {response.json()['id']}"
    print("Get asset by ID test passed.")

def test_update_asset(asset_id):
    url = f"{BASE_URL}/assets/{asset_id}"
    payload = {
        "name": "Laptop",
        "type": "Electronics",
        "location": "Branch Office"
    }
    response = requests.put(url, json=payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["location"] == "Branch Office", "Expected updated location to be 'Branch Office'"
    print("Update asset test passed.")

def test_delete_asset(asset_id):
    url = f"{BASE_URL}/assets/{asset_id}"
    response = requests.delete(url)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Delete asset test passed.")

def run_tests():
    print("Running tests...")
    asset_id = test_create_asset()
    test_get_assets()
    test_get_asset(asset_id)
    test_update_asset(asset_id)
    test_delete_asset(asset_id)
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()
