# 3. На ввод подается строка. Нужно узнать является ли строка палиндромом.
# (Палиндром - строка которая читается одинаково с начала и с конца.)

s = input('Введите строку: ')
if s == s[::-1]: #проверяем условие равна ли строка строке наоборот
    print('Строка является палиндромом') #выводим, если условие вполняется
else:
    print('Строка не является палиндромом') #выводим, если условие не вполняется

