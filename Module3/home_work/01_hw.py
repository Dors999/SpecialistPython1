# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
i=0
string=""
while i!=len(names):
    string=string+names[i]+", "
    i+=1
print(string[0:(len(string)-2)])

#names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
#names_string = ', '.join(names)
#print (names_string)
