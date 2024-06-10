import requests
import uuid

BASE_URL = "http://127.0.0.1:8000"


def test_create_department():
    response = requests.post(f"{BASE_URL}/departments/", json={"name": "IT"})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    department_id = response.json()["id"]
    print("Create department test passed.")
    return department_id


def test_get_departments():
    response = requests.get(f"{BASE_URL}/departments/")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Get departments test passed.")


def test_get_department_by_id(department_id):
    response = requests.get(f"{BASE_URL}/departments/{department_id}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Get department by ID test passed.")


def test_update_department(department_id):
    response = requests.put(f"{BASE_URL}/departments/{department_id}", json={"name": "HR"})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Update department test passed.")


def test_delete_department(department_id):
    response = requests.delete(f"{BASE_URL}/departments/{department_id}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Delete department test passed.")


def test_create_user(department_id):
    response = requests.post(f"{BASE_URL}/users/",
                             json={"name": "John Doe", "username": "jdoe", "department_id": department_id})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    user_id = response.json()["id"]
    print("Create user test passed.")
    return user_id


def test_get_users():
    response = requests.get(f"{BASE_URL}/users/")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Get users test passed.")


def test_get_user_by_id(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Get user by ID test passed.")


def test_update_user(user_id, department_id):
    response = requests.put(f"{BASE_URL}/users/{user_id}",
                            json={"name": "Jane Doe", "username": "jdoe2", "department_id": department_id})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Update user test passed.")


def test_delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Delete user test passed.")


def test_create_asset(user_id):
    unique_sr = str(uuid.uuid4())
    response = requests.post(f"{BASE_URL}/assets/", json={
        "name": "Laptop",
        "type": "Electronics",
        "serial_nr": unique_sr,
        "user_id": user_id
    })
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    asset_id = response.json()["id"]
    print("Create asset test passed.")
    return asset_id


def test_get_assets():
    response = requests.get(f"{BASE_URL}/assets/")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Get assets test passed.")


def test_get_asset_by_id(asset_id):
    response = requests.get(f"{BASE_URL}/assets/{asset_id}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Get asset by ID test passed.")


def test_update_asset(asset_id, user_id):
    response = requests.put(f"{BASE_URL}/assets/{asset_id}", json={
        "name": "Desktop",
        "type": "Electronics",
        "serial_nr": "XYZ987654",
        "user_id": user_id
    })
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Update asset test passed.")


def test_delete_asset(asset_id):
    response = requests.delete(f"{BASE_URL}/assets/{asset_id}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Delete asset test passed.")


def run_tests():
    # Department tests
    department_id = test_create_department()
    test_get_departments()
    test_get_department_by_id(department_id)
    test_update_department(department_id)
    test_delete_department(department_id)

    # Create department again for user and asset tests
    department_id = test_create_department()

    # User tests
    user_id = test_create_user(department_id)
    test_get_users()
    test_get_user_by_id(user_id)
    test_update_user(user_id, department_id)
    test_delete_user(user_id)

    # Create user again for asset tests
    user_id = test_create_user(department_id)

    # Asset tests
    asset_id = test_create_asset(user_id)
    test_get_assets()
    test_get_asset_by_id(asset_id)
    test_update_asset(asset_id, user_id)
    test_delete_asset(asset_id)


if __name__ == "__main__":
    run_tests()
