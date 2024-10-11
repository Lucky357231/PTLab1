import json
from Types import DataType
from DataReader import DataReader


class JSONDataReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
            return {}
        except json.JSONDecodeError:
            print("Error decoding the JSON file.")
            return {}

    def get_student_scores(self, student_name):
        return self.data.get(student_name, "Student not found")

    def get_all_students(self):
        return list(self.data.keys())

    def get_subject_scores(self, subject_name):
        result = {}
        for student, subjects in self.data.items():
            if subject_name in subjects:
                result[student] = subjects[subject_name]
        return result
