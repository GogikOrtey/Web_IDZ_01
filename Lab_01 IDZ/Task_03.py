import sqlite3
from datetime import datetime

def get_days_between_dates(date1, date2):
    date1 = datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.strptime(date2, '%Y-%m-%d')
    delta = date2 - date1
    return delta.days


# Открываю БД
con = sqlite3.connect("booking_py_01.sqlite")
f_damp = open('D:/Рабочий стол/Учёба 4й курс 2023/Сетевые/1 лаба - работа с SQLite/Lab_01 IDZ/booking.db','r', encoding ='utf-8-sig')

# Загружаю данные
damp = f_damp.read()
f_damp.close()
con.executescript(damp)

# Выполняю SQL-запрос
con.commit()
cursor = con.cursor()
cursor.execute('''
SELECT DISTINCT * 
FROM room_booking
WHERE status_id = 1
''')
 
#print(cursor.fetchall())

count_str = 0

print("id | Комната | Гость | Кол-во дней в номере")

# for row in cursor.fetchall():
#     for i in range(len(row)-3):
#         if(i == 0): 
#             if(count_str < 9): print(row[i], end="    ")
#             else: print(row[i], end="   ")
#         else: print(row[i], end="       ")
#         print(get_days_between_dates(row[-3], row[-2]), end="")
#     print("     ", end="")
#     #if int(str(row[3])) > 6: print("Высокий")
#     print()
#     count_str+=1

data_list = []

# Перегоняю все данные в нужный мне двумерный лист
for row in cursor.fetchall():
    current_row = []
    # Не добавляю в массив 3 последних столбца из запроса
    for i in range(len(row)-3):
        current_row.append(row[i])
    # Добавляю количество дней - разницу между датой заселения и датой веселения
    current_row.append(get_days_between_dates(row[-3], row[-2]))
    data_list.append(current_row)
    count_str += 1

# for row in data_list:
#     print(row)

# Сортирую полученный массив, по последнему элементу каждоого подмассива
sorted_data_list = sorted(data_list, key=lambda x: x[-1])

# print("\n\n\n")
# for row in sorted_data_list:
#     print(row)

max_day_in_room = sorted_data_list[-1][-1]
list_finalist = []

for row in reversed(sorted_data_list):
    if(row[-1] == max_day_in_room):
        list_finalist.append(row)
    else: break

print("\nКоличество строк: ", count_str)
print("Максимально в одной комнате проживали количество дней: ", max_day_in_room)
print("Вот эти люди, и все номера, в которых они проживали:\n")

## Получаю уникальные id посетителей, из выбранных данных
list_gustes_id = []

for row in list_finalist:
    #print(row)
    list_gustes_id.append(row[-2])

unique_list_gustes_id = list(set(list_gustes_id))

#print(unique_list_gustes_id)

final_information_list = []

# Выполняю SQL-запрос, для каждого такого id
for id in unique_list_gustes_id:
    con.commit()
    cursor = con.cursor()
    quverty = f'''
    SELECT DISTINCT guest.guest_name, type_room_name --*, guest.guest_id
    FROM room_booking, room, type_room, guest
    WHERE status_id = 1 
        AND guest.guest_id = {id}
        AND room.room_id = room_booking.room_id
        AND room.type_room_id = type_room.type_room_id
        AND room_booking.guest_id = guest.guest_id
    '''
    cursor.execute(quverty)

    #print(cursor.fetchall())
    final_information_list.append(cursor.fetchall())

final_information_list.sort(key=lambda x: x[0][0].split()[0])

for row in final_information_list:
    print(row)

#print(final_information_list)