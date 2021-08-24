# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле.
# Пробельные символы: " " - пробел, "\n" - перенос строки, "\t" - табуляция
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется ровно одной пустой строкой от предыдущего и после последнего нет пустой строки

path = "dir/limericks.txt"  # вместо dir подставь название папки с файлом.
# Или удалите dir, если limericks.txt в тойже папке что и текущий файл

# Открываем файл на чтение
f = open(path, "r")
# В переменную line считываем строку за стройкой из файла(f)
for line in f:
    ...

# Подсказка: пустые строки выглядят так "\n". Помните? Строка считывается вместе с символом переноса!
# Применение метода "\n".rstrip() --> "" вернет вам пустую строку, строку из НУЛЯ символов.

import string
#функция удаления пробельных символов
def remove_whitespace(in_string: str):
    return in_string.translate(str.maketrans(dict.fromkeys(string.whitespace)))
#открытие файла
f = open("limericks.txt","r",encoding="utf-8")
#печатаем файл построчно
for line in f:
    line = line.rstrip()
    print(line)
count = 0
f.seek(0)
#удаляем символы и считаем общее количество символов
for line in f:
    line = remove_whitespace(line)
    count += len(line)
print("Simvolov vsego=:", count)
count = 1
f.seek(0)
#считаем общее количество стихотворений
for line in f:
    if line=="\n":
        count+=1
print("Stihotvoreniy vsego=",count-1)
