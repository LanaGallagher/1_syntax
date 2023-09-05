# ***Коллекции***

# Список (list)

# список - это упорядоченная (проиндексированная), изменяемая (мутабельная) коллекция

# обьекты внутри списка - элементы
# каждый элемент проиндексирован

# Создание пустого списка
lst_0 = []
lst_0 = list()

# Создание предварительно заполненного списка
lst_1 = [3, 100, 26, 0, -1, -777]

lst_2 = [10, 20, 3.14, "python", [1,2,3], 'A']

lst_3 = list("python. Hello, World!")

# добавление элемента (объекта) в список (используем "метод"). Метод - это встроенные внутренние функции
# print(lst_0)

lst_0.append(1000)
lst_0.append("hello")
lst_0.append([10,20,30])

# чтение значений элементов
# прямая индексация
val_0 = lst_3[0]

# обратная индексация
val_0 = lst_3[-1]
val_0 = lst_3[-5]

# чтение значения элемента вложенного списка
lst_4 = [[10,20], [1,2,3], [1000]]

val_1 = lst_4[1][0]

# замена значения
lst_5 = list("Hello, World!")

# print(f"Исходный список: {lst_5}")

lst_5[0] = 'h'

# print(f"Измененный список: {lst_5}")

# удаление элемента
# по индексу
del lst_5[1]

# удаление по значению
# lst_5.remove('l')
# lst_5.remove('!')
# lst_5.remove('r')

# очистка списка

# print(lst_5)

lst_5.clear()

# print(lst_5)

# срезы списка
lst_6 = list("Hello, World!")

print(lst_6)
# print(len(lst_6))

# срез от начала до конца
s_1 = lst_6[0:13] 
s_1 = lst_6[:]

# срез от начала до индекса В (не включительно) 
s_1 = lst_6[:7]

# срез от индекса А до конца
s_1 = lst_6[4:]

# срез от индекса А до индекса В (не включительно)
s_1 = lst_6[4:9]

print(s_1)

# срез по отрицательным индесам
# шаг среза

# самостоятельно повторить
