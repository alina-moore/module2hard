import random


def code():
    number = range(3, 21)
    n = random.choice(number)
    return n


n = code()  # случайно генерирует числа от 3 до 20 в первом камне
print("Число из первой каменной вставки:", n)

spisok = [*range(1, 21)]  # создает список от 1 до 20

# print(spisok) - проверка


# создаем пары сумм, используя числа от 1 до 20
pary = []
for i in range(len(spisok)):
    for j in range(i + 1, len(spisok)):
        summa_pary = spisok[i] + spisok[j]
        # ищем те, что кратны
        if n % summa_pary == 0:
            pary.append((spisok[i], spisok[j]))
            # summa.append(summa_pary) - нет связи с самими парами - устарел

        # пары сумм от 1 до 20 ВСЕ ВОЗМОЖНЫЕ - устарел
        # print(str(spisok[i]), str(spisok[j]))

        # без пробелов вариант ниже - устарел
        # summa += f"{spisok[i]}{spisok[j]}"

# вывод
if pary:
    print("Верный пароль:")
    for result in pary:
        # print(result) - перенос, скобки, пробелы - все лишние
        print(''.join(map(str, result)), end='')

# for kratno in summa:
#     x, y, summa_pary = kratno
#     if n % summa_pary == 0:
#         print(f"{n} кратен сумме паре {x} и {y}, что дает {summa_pary}")
#     else:
#         break
#         не подошло УСТАРЕЛО
