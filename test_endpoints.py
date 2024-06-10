import requests

BASE_URL = "http://localhost:8000"


def test_create_department():
    url = f"{BASE_URL}/departments/"
    payload = {
        "name": "IT Department"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    department_id = response.json()["id"]
    print("Create department test passed.")
    return department_id


def test_get_departments():
    url = f"{BASE_URL}/departments/"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert isinstance(response.json(), list), "Expected a list"
    print("Get departments test passed.")


def test_get_department(department_id):
    url = f"{BASE_URL}/departments/{department_id}"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()[
               "id"] == department_id, f"Expected department ID {department_id}, got {response.json()['id']}"
    print("Get department by ID test passed.")


def test_create_user(department_id):
    url = f"{BASE_URL}/users/"
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "department_id": department_id
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    user_id = response.json()["id"]
    print("Create user test passed.")
    return user_id


def test_get_users():
    url = f"{BASE_URL}/users/"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert isinstance(response.json(), list), "Expected a list"
    print("Get users test passed.")


def test_get_user(user_id):
    url = f"{BASE_URL}/users/{user_id}"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["id"] == user_id, f"Expected user ID {user_id}, got {response.json()['id']}"
    print("Get user by ID test passed.")


def test_create_asset(user_id):
    url = f"{BASE_URL}/assets/"
    payload = {
        "name": "Laptop",
        "type": "Electronics",
        "location_id": 1,
        "serial_number": "ABC123456",
        "purchase_date": "2023-01-01",
        "warranty_expiration": "2025-01-01",
        "status": "active",
        "assigned_to": user_id,
        "last_maintenance": "2023-06-01",
        "notes": "Brand new laptop"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    asset_id = response.json()["id"]
    print("Create asset test passed.")
    return asset_id


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


def run_tests():
    print("Running tests...")
    department_id = test_create_department()
    test_get_departments()
    test_get_department(department_id)

    user_id = test_create_user(department_id)
    test_get_users()
    test_get_user(user_id)

    asset_id = test_create_asset(user_id)
    test_get_assets()
    test_get_asset(asset_id)

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
