# Задание 1
# Вывести информацию о номерах с видом на море. Указать название номера, название типа и цену. 
# Столбцы назвать Номер, Тип_номера, Цена соответственно. Информацию отсортировать сначала по 
# возрастанию цены, а затем по названию номера в алфавитном порядке.

# Пояснение. По названию номера можно определить вид из окна. Название номера состоит из 6 символов,
# если последняя цифра нечетная (1, 3, 5, 7 или 9), то у номера вид на море, если же цифра четная, 
# то у номера вид на горы. Например:
# Л-0103 - номер с видом на море;
# П-1214 - номер с видом на горы.

import sqlite3
# создаем базу данных и устанавливаем соединение с ней
con = sqlite3.connect("booking_py_01.sqlite")
# открываем файл с дампом базой двнных
f_damp = open('D:/Рабочий стол/Учёба 4й курс 2023/Сетевые/1 лаба - работа с SQLite/Lab_01 IDZ/booking.db','r', encoding ='utf-8-sig')


# читаем данные из файла
damp = f_damp.read()
# закрываем файл с дампом
f_damp.close()
# запускаем запросы
con.executescript(damp)
# сохраняем информацию в базе данных

con.commit()
cursor = con.cursor()
cursor.execute('''
    SELECT room.room_name AS "Номер", 
        type_room.type_room_name AS "Тип номера", 
        type_room.price AS "Цена" 
    FROM room 
    JOIN type_room ON room.room_id = type_room.type_room_id 
    ''')
# cursor.execute('SELECT room.room_name AS "Номер", type_room.type_room_name AS "Тип номера", type_room.price AS "Цена" FROM room JOIN type_room ON room.room_id = type_room.type_room_id WHERE (CONVERT(INT, SUBSTRING(room.room_name, LEN(room.room_name))) % 2) = 1')

# Я никак не могу добиться того, что бы sqlite корректно обрабатывал моё условие на вывод (которое WHERE)
# Тогда я пошёл дальше:
 
#print(cursor.fetchall())

count_str = 0

print("Номер       Тип номера              Цена")

for row in cursor.fetchall():
    # Проверяю, что у первого атрибута строки его последний символ, преобразованный в число - нечёнтый
    if  int(str(row[0][-1])) % 2 == 1: 
        count_str+=1
        print(row)

print("\nКоличество строк: ", count_str)

# ЕСЛИ Я ЧЕГО-ТО НЕ ПОНЯЛ, И ИЗ-ЗА ЭТОГО СДЕЛАЛ НЕПРАВИЛЬНО - ВСЕ ВОПРОСЫ К СОСТАВИТЕЛЮ ЗАДАНИЙ :)

c = input()