# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")

# TODO: your code here

print("На складе больше всего товаров брэнда(ов): ")

# TODO: your code here

print("На складе самый дорогой товар брэнда(ов): ")

# TODO: your code here


# Данные о товарах на складе хранятся в словаре
dictionary = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
temp=0
i=0
brand=[]
brand_temp=[]
brand_count=[]
brand_price=[]
for i in range(len(dictionary)):
    for key, value in dictionary[i].items():
        if key=="brand":#поиск всех брендов
            brand_temp.append(value)
        if key=="price":#поиск всех цен
            brand_price.append(value)
brand = list(set(brand_temp))

print("Товары на складе представлены брэндами: ",brand)
while temp<len(brand_price)-1: #поиск максимальной цены
    if brand_price[temp]>=brand_price[temp+1]:
        brand_price[temp+1]=brand_price[temp]
        del brand_price[temp]
        i-=1
    else:
        del brand_price[temp]
        i-=1
    i+=1

for item in brand:                                                                  #поиск количества предметов каждого бренда
    count = 0
    for i in range(len(dictionary)):
        for key, value in dictionary[i].items():
            if key=="brand":
                if value==item:
                    count+=1
    brand_count.append(count)
temp=0
count=0
i=0

while i!=len(brand_count): #поиск максимального количества предметов
    if count < int(brand_count[i]):
        count=int(brand_count[i])
    i+=1
i=0

print("На складе больше всего товаров брэнда(ов): ")
while i!=len(brand_count):  # вывод на экран брендов максимального количества предметов
    if count == brand_count[i]:
        print(brand[i])
    i+=1

print("На складе самый дорогой товар брэнда(ов): ")
i=0
count=0
for i in range(len(dictionary)):
    for key, value in dictionary[i].items():
        if key=="price":#поиск места в списке самого дорогого бренда
            if value==brand_price[0]:
                count=i
for key, value in dictionary[count].items():
    if key=="brand":
        print(value)
