# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
new_names=[]
i=0
len_temp=0
while i<len(names)-1:
    print(names[i])
    if len(names[i])>=len(names[i+1]):
        names[i+1]=names[i]
        del names[i]
        i-=1
    else:
        del names[i]
        i-=1
    i+=1


print(names)
