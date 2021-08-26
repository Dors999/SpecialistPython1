# Вы написали программу для работы с сотрудниками и вам ее необходимо протестировать.
# Для теста нужны большие списки сотрудников (100+).
# Вбивать вручную столько данных займет очень много времени.
# Напишите программу, генерирующую списки сотрудников со следующими параметрами:
# 1. Имя
# 2. Фамилия
# 3. Возраст
# 4. Профессия
# 5. Зарплата
# Примечание: Данные сгенерированных сотрудников могут повторяться
import random

name=["Alex","Mihail","Sergey","Ruslan"]
fam=["Galp","Dors","Podolsk","Kamyshnikov","Ohota"]
prof=["IT","stroitel","montagnik","rukovoditel"]
for _ in range(100):
    print(f"1. {random.choice(name)} \n2. {random.choice(fam)} \n3. {random.randint(18,60)} \n4. {random.choice(prof)} \n5. {random.randint(18,60)} \n")
