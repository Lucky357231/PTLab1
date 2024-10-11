class Students:
    def __init__(self, students: dict):
        self.students = students  # Словарь для хранения данных о студентах

    def count_academic_debts(self):
        """Подсчитать количество студентов с академическими задолженностями."""
        count = 0
        for scores in self.students.values():
            if any(score < 61 for score in scores.values()):
                count += 1
        return count
