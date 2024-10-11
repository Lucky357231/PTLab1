import os
import pytest
from src.JSONDataReader import JSONDataReader


# Получаем текущий рабочий каталог
current_dir = os.path.dirname(os.path.abspath(__file__))
# Определяем путь к students.json в папке data
json_file_path = os.path.join(current_dir, '../data/students.json')


def test_load_data():
    reader = JSONDataReader(json_file_path)  # Используем правильный путь
    assert isinstance(reader.data, dict)
    assert "Иванов Иван Иванович" in reader.data
    assert "математика" in reader.data["Иванов Иван Иванович"]


def test_get_student_scores():
    reader = JSONDataReader(json_file_path)  # Используем правильный путь
    assert reader.get_student_scores("Иванов Иван Иванович") == {
        "математика": 57,
        "литература": 100,
        "программирование": 91
    }
    assert reader.get_student_scores("Неизвестный") == "Student not found"


def test_get_all_students():
    reader = JSONDataReader(json_file_path)  # Используем правильный путь
    expected_students = [
        "Иванов Иван Иванович", "Петров Петр Петрович",
        "Сидоров Сергей Сергеевич", "Кузнецова Мария Ивановна",
        "Алексеева Анна Николаевна", "Морозов Олег Дмитриевич"
    ]
    assert set(reader.get_all_students()) == set(expected_students)


def test_get_subject_scores():
    reader = JSONDataReader(json_file_path)  # Используем правильный путь
    assert reader.get_subject_scores("математика") == {
        "Иванов Иван Иванович": 57,
        "Петров Петр Петрович": 28,
        "Сидоров Сергей Сергеевич": 92,
        "Алексеева Анна Николаевна": 80,
        "Морозов Олег Дмитриевич": 69
    }
    assert reader.get_subject_scores("неизвестный предмет") == {}
