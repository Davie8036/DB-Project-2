# filepath: /c:/Users/Home/Desktop/DB Project/populate_db.py
import requests

BASE_URL = "http://127.0.0.1:8000"

def populate_data():
    # Генерация тестовых данных
    response = requests.post(f"{BASE_URL}/generate_sample_data")
    print(response.json())

if __name__ == "__main__":
    populate_data()