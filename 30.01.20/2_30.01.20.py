# 2* Дан отсортированный список. Реализуйте бинарный поиск.
L = [x for x in range(20, 0, -1)]
print(L)
n = int(input('Введите элемент для поиска в списке: '))

i_left = 0
i_right = len(L) - 1

while i_right - i_left >= 0:
    i_med = i_left + (i_right - i_left) // 2
    if n == L[i_med]:
        print('элемент входит в список и стоит на позиции: ', i_med)
        break
    elif L[i_left] < L[i_right]:
        if n > L[i_med]:
            i_left = i_med + 1
        else:
            i_right = i_med - 1
    else:
        if n < L[i_med]:
            i_left = i_med + 1
        else:
            i_right = i_med - 1
else:
    print('элемент не входит в список')