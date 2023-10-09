import sqlite3
con = sqlite3.connect("booking_py_01.sqlite")
f_damp = open('D:/Рабочий стол/Учёба 4й курс 2023/Сетевые/1 лаба - работа с SQLite/Lab_01 IDZ/booking.db','r', encoding ='utf-8-sig')


damp = f_damp.read()
f_damp.close()
con.executescript(damp)

con.commit()
cursor = con.cursor()
cursor.execute('''
SELECT room.room_id, room.room_name, room.type_room_id, COUNT(room_booking.guest_id) AS guest_count
FROM room
JOIN room_booking ON room.room_id = room_booking.room_id
GROUP BY room.room_id, room.room_name, room.type_room_id
''')
 
#print(cursor.fetchall())

count_str = 0

print("id | Номер | Тип номера | Количество | Спрос")

for row in cursor.fetchall():
    for i in range(len(row)):
        if(i == 0): 
            if(count_str < 9): print(row[i], end="    ")
            else: print(row[i], end="   ")
        else: print(row[i], end="       ")
    print("     ", end="")
    if int(str(row[3])) > 6: print("Высокий")
    elif int(str(row[3])) < 4: print("Низкий")
    else: print("Средний")
    #print()
    count_str+=1
    # print(row)

print("\nКоличество строк: ", count_str)
