import os
import random
import numpy
import codecs

num = int(input("Введите количество строк в файле F1 (более 10:\n"))
list_alphabet = ("а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я А Б В Г Д Е Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я").split()
list_sogl = ("б в г д ж з й к л м н п р с т ф х ц ч ш щ Б В Г Д Ж З Й К Л М Н П Р С Т Ф Х Ц Ч Ш Щ").split()
file_input = codecs.open("F1", 'w', 'utf-16')
for i in range(num):
    temp_len = random.randint(1,100)
    temp_str = ''
    for j in range(temp_len):
        temp_str += list_alphabet[random.randint(0,len(list_alphabet) - 1)]
    file_input.write(temp_str+"\n")
file_input.close()
line_from = int(input("Введите с какой строки копировать: \n"))
line_till = int(input("Введите по какую строку копировать: \n"))
file_input = codecs.open("F1", 'r', 'utf-16')
file_output = codecs.open("F2", 'w', 'utf-16')
read_list = file_input.read().split('\n')
str_count = ""
counter = 0
for i in range(line_from - 1, line_till):
    str_count += read_list[i]
    file_output.write(read_list[i] + "\n")
for i in range(len(str_count)):
    if str_count[i] in list_sogl:
        counter += 1
print("В скопированных строках ", counter, " согласных букв.")
file_input.close()
file_output.close()