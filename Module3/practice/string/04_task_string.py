# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

text = input("text: ")
text=text+"."
i=0
k=0
slova=0
while text[i]!=".":
   if text[i]!=" ":
       k+=1
   elif k>5:
       slova+=1
       k=0
   else:
       k=0
   i+=1
print("kolishestvo slov>5 simvolov",slova)
