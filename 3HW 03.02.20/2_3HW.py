# 2. Дана строка S. Нужно распечатать её подстроками длиной w. Например S=”ABCDEFGHIJKLIMNOQRSTUVWXYZ” и w=4 - выход
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

S = input('Введите строку: ')
w = int(input('Введите длину подстрок для распечатки: '))

# создаем цикл, где пройдемся от 0 до длины строки с шагом, равным размеру подстрок w,
# чтобы определять начало распечатки подстроки
for i in range(0, len(S), w):
    # печатаем подстроку с помошью среза
    print(S[i: i+w])