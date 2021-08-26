# Доработайте предыдущую программу так, чтобы каждый сгенерированный сотрудник
# был уникальным(не должны повторяться комбинации Имя + Фамилия).
import random

name=["Alex","Mihail","Sergey","Ruslan"]
fam=["Galp","Dors","Podolsk","Kamyshnikov","Ohota"]
prof=["IT","stroitel","montagnik","rukovoditel"]
for el in name:
    for fa in fam:
        print(f"1. {el} \n2. {fa} \n3. {random.randint(18,60)} \n4. {random.choice(prof)} \n5. {random.randint(18000,60000)} \n")
