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
форма), пример: !{имя + 1}

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

Файл с тестированием всех функций интерпретатора: https://github.com/Vector-363/Homework_3/blob/main/Testing.py

Пример запуска кода: 

![image](https://github.com/user-attachments/assets/57d23911-2da4-4105-8863-3fe08e0912fd)

Пример входного файла: 

     #Вычисление константного выражения на этапе транляции:
     const:
        f: 5
        h: "!{f+5}"
     #Для константных вычислений определены операции и функции:
     constants:
        a: 3
        b: 4
        c: 1.123
        d: 2.12
     calculations:
     sum:
        #1. Сложение:
        sum: "!{a+b}"
     sub:
        #2. Вычитание:
        sub: "!{a-b}"
     mul:
        #3. Умножение:
        mul: "!{a*b}"
     div:
        #4. Деление:
        div: "!{a/b}"
     paralel:
        # Параллельное вычисление:
        paralel: "!{(a+b)*(a-b)}"
     num:
        -1
        -2
        -3
        -4
     #5. len():
        len_plus_one: "!{len(num)}"

Выходной файл: 

![image](https://github.com/user-attachments/assets/7f4f11e8-e326-4bee-a7cd-f823a3c15d46)









