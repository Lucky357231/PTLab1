import pytest
from Students import Students


class TestStudents:

    def setup_method(self):
        """Подготовка данных для тестов."""
        # Пример данных о студентах
        self.students_data = {
            "Иванов Иван Иванович": {
                "математика": 57,
                "литература": 100,
                "программирование": 91
            },
            "Петров Петр Петрович": {
                "математика": 68,
                "литература": 50,
                "программирование": 80
            },
            "Сидоров Сергей Сергеевич": {
                "математика": 92,
                "литература": 88,
                "программирование": 94
            },
            "Кузнецова Мария Ивановна": {
                "математика": 45,
                "литература": 72,
                "программирование": 60
            },
            "Алексеева Анна Николаевна": {
                "математика": 100,
                "литература": 95,
                "программирование": 98
            },
            "Морозов Олег Дмитриевич": {
                "математика": 70,
                "литература": 65,
                "программирование": 80
            }
        }
        self.students = Students(self.students_data)

    def test_count_academic_debts(self):
        """Тест на подсчет студентов с академическими задолженностями."""
        assert self.students.count_academic_debts() == 3  \
            # Ожидается 3 студента

    def test_no_academic_debts(self):
        """Тест на случай, когда нет студентов с задолженностями."""
        students_data_no_debts = {
            "Иванов Иван": {
                "математика": 90,
                "литература": 80
            },
            "Петров Петр": {
                "математика": 85,
                "литература": 95
            }
        }
        students_no_debts = Students(students_data_no_debts)
        assert students_no_debts.count_academic_debts() == 0
        # Ожидается, что нет задолженностей

    def test_all_students_with_academic_debts(self):
        """Тест на случай, когда все студенты имеют задолженности."""
        students_data_all_debts = {
            "Иванов Иван": {
                "математика": 50,
                "литература": 40
            },
            "Петров Петр": {
                "математика": 55,
                "литература": 30
            },
        }
        students_all_debts = Students(students_data_all_debts)
        assert students_all_debts.count_academic_debts() == 2
        # Ожидается, что все студенты с долгами


if __name__ == '__main__':
    pytest.main()
