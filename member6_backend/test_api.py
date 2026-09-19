import requests


BASE_URL = "http://127.0.0.1:5000"


def test_home():
    response = requests.get(BASE_URL)

    print("Home API Status:", response.status_code)
    print("Home API Response:", response.json())

    assert response.status_code == 200


def test_chat():
    data = {
        "question": "What is the exam timetable?"
    }

    response = requests.post(
        BASE_URL + "/api/chat",
        json=data
    )

    print("Chat API Status:", response.status_code)
    print("Chat API Response:", response.json())

    assert response.status_code == 200
    assert response.json()["intent"] == "EXAM"


def test_admin_update():
    data = {
        "course": "B.Tech CSE",
        "fees": "50000",
        "attendance": "75%"
    }

    response = requests.post(
        BASE_URL + "/api/admin/update",
        json=data
    )

    print("Admin Update Status:", response.status_code)
    print("Admin Update Response:", response.json())

    assert response.status_code == 200


def test_admin_data():
    response = requests.get(
        BASE_URL + "/api/admin/data"
    )

    print("Admin Data Status:", response.status_code)
    print("Admin Data Response:", response.json())

    assert response.status_code == 200


if __name__ == "__main__":
    test_home()
    test_chat()
    test_admin_update()
    test_admin_data()

    print("\nAll API tests completed successfully!")