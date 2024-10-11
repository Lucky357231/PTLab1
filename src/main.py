# -*- coding: utf-8 -*-
import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from JSONDataReader import JSONDataReader
from Students import Students


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument(
        "-p",
        dest="path",
        type=str,
        required=True,
        help="Path to datafile"
    )
    args = parser.parse_args(args)
    return args.path


def main() -> None:
    path = get_path_from_arguments(sys.argv[1:])

    # Используем JSONDataReader для загрузки данных
    reader = JSONDataReader(file_path=path)  # Передаем путь к файлу
    students_data = reader.data  # Получаем данные о студентах

    # Выводим считанные данные (для отладки)
    print("Students Data: ", students_data)

    # Инициализируем класс Students с загруженными данными
    students = Students(students_data)

    # Подсчитываем студентов с академическими задолженностями
    academic_debts_count = students.count_academic_debts()

    # Выводим результат
    print(
        f"Количество студентов с академическими задолженностями: "
        f"{academic_debts_count}"
    )


if __name__ == "__main__":
    main()
