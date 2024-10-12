<h1 align="center">Лабораторная №1 по дисциплине "Технологии программирования"</h1>

## Знакомство с системой контроля версий Git и инструментом CI/CD GitHub Actions

### Цели работы:

1. Познакомиться c распределенной системой контроля версий кода Git и ее функциями;
2. Познакомиться с понятиями «непрерывная интеграция» (CI) и «непрерывное развертывание»
   (CD), определить их место в современной разработке программного обеспечения;
3. Получить навыки разработки ООП-программ и написания модульных тестов к ним на
   современных языках программирования;
4. Получить навыки работы с системой Git для хранения и управления версиями ПО;
5. Получить навыки управления автоматизированным тестированием программного обеспечения,
   расположенного в системе Git, с помощью инструмента GitHub Actions.


### Постановка задачи:

1. Выберите для Вашего проекта тип лицензии и добавьте файл с лицензией в проект.
2. Добавьте в проект файл .gitignore и сформируйте его содержимое.
3. Добавьте в проект еще один класс – наследник класса DataReader, который должен
обрабатывать входной файл определенного формата (согласно индивидуальному варианту, см.
таблицу). Составьте модульные тесты для методов этого класса, постарайтесь покрыть тестами
максимально возможный объем кода. Для работы с этим заданием создайте новую ветку кода на основе
главной и фиксируйте в нее весь программный код в процессе разработки. Добейтесь выполнения всех
тестов проекта, после чего объедините текущую ветку кода с главной.
4. Добавьте в проект класс, реализующий расчет определенных характеристик студентов
(согласно индивидуальному варианту, см. таблицу). Составьте модульные тесты для методов этого
класса, постарайтесь покрыть тестами максимально возможный объем кода. Для работы с этим
заданием создайте новую ветку кода на основе главной и фиксируйте в нее весь программный код в
процессе разработки. Добейтесь выполнения всех тестов проекта, после чего объедините текущую
ветку кода с главной.
5. Составьте UML-диаграмму классов итогового проекта.
6. Проанализируйте полученные результаты и сделайте выводы.

### Описание проекта:

В лабораторной работе используется проект, читающий список студентов и последующим выводом на экран количество студентов, имеющих академические задолженности.
Проект написан на языке программирования Python 3, модульное тестирование в нем осуществляется с помощью библиотеки pytest.
Помимо этого была использована система контроля версий (VCS), а именно github, и ее система автоматических тестов.

### используемые языки / библиотеки / технологии:

<p>Python 3. x</p>
<p>Библиотеки: pycodestyle, pytest, argparse, os, sys, JSON</p>
<p>Используемые технологии: Python, Git, GitHub Actions</p>

### Индивидуальное задание:

<h1 align="center">4 вариант</h1>

<p>-JSON</p>
-Рассчитать и вывести на экран количество студентов,
имеющих академические задолженности (имеющих балл
< 61 хотя бы по одному предмету).

### Ход работы:

Выполнение кода ветки task_students прошло успешно
![image](https://github.com/Lucky357231/PTLab1/blob/main/img/photo_2024-10-12_02-08-13.jpg?raw=true)

Проверка кода ветки task_students прошла успешно
![image](https://github.com/Lucky357231/PTLab1/blob/main/img/photo_2024-10-12_02-07-58.jpg?raw=true)

### UML-диаграммы:

![image](https://github.com/Lucky357231/PTLab1/blob/main/img/Screenshot_7.jpg?raw=true)

### Вывод:

В ходе лабораторной работы я изучил системы контроля версий Git и концепции CI/CD. 
Освоил разработку ООП-программ, реализовал классы для выполнения заданий, написал модульные тесты, которые покрывают значительную часть кода, и составил UML диаграмму классов.
