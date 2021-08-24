# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Формат файла: Цены товаров представлены целыми или вещественными числами.
#               Цены разделены одним или более пробельными символами.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара

# Совет: сначала считайте все цены из файла, сохраните в список,
# преобразовав каждую цену к числу(цены в файле хранятся в виде строк)
# А затем, работам с привычным списком, выполните задания
prices = []

# Подсказка: для преобразования строки в список вспомните про метод строки .split()
import string
prices = []
f = open("sold.txt","r",encoding="utf-8")
for line in f:
    line = line.rstrip()
    prices+=line.split()

price_min = float(prices[0])
price_max = float(prices[0])
price = 0
for i in prices:
    if price_max<float(i):
        price_max=float(i)
    if price_min>float(i):
        price_min=float(i)
    price+=float(i)
print("MAX=",price_max)
print("MIN=",price_min)
print("Vsego=",price)
print(prices)
