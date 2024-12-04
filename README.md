# Homework_3

Вариант №26

Задание №3
Разработать инструмент командной строки для учебного конфигурационного
языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из
входного формата в выходной. Синтаксические ошибки выявляются с выдачей
сообщений.

Входной текст на языке yaml принимается из файла, путь к которому задан
ключом командной строки. Выходной текст на учебном конфигурационном
языке попадает в файл, путь к которому задан ключом командной строки.

Однострочные комментарии:

' Это однострочный комментарий

Массивы:

array( значение, значение, значение, ... )

Словари:

$[

 имя : значение,
 
 имя : значение,
 
 имя : значение,
 
 ...
 
]

Имена:

[a-zA-Z]+

Значения:

• Числа.

• Массивы.

• Словари.

Объявление константы на этапе трансляции:

имя is значение

Вычисление константного выражения на этапе трансляции (инфиксная
форма), пример:

!{имя + 1}
Результатом вычисления константного выражения является значение.
Для константных вычислений определены операции и функции:

1. Сложение.
2. Вычитание.
3. Умножение.
4. Деление.
5. len().

Все конструкции учебного конфигурационного языка (с учетом их
возможной вложенности) должны быть покрыты тестами. Необходимо показать 2
примера описания конфигураций из разных предметных областей.

Описание функций:

parse_config(yaml_data, context={}, is_top_level=True) - функция для конвертации языка

evaluate_expression(expression, context) - функция для константных вычислений

cut_output(input_string) - функция для поправки синтаксиса

Файл с тестированием всех функций интерпретатора: 
