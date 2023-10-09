# Садиев С.И., проживающий в номере С-0226 с 4 ноября 2020

# Создать новую таблицу bill

# Тип номера
# Навзание номера
# Дату заселения и выселения
# Цена проживания за день

# Посчитать стоимость проживания за все дни

# Название услуги
# Дата получения услуги (м/б несколько дат)
# Стоимость услуги

# Посчитать сумму за кол-во услуг

# Посчиать всю сумму (Итого)

import sqlite3
con = sqlite3.connect("booking_py_01.sqlite")
f_damp = open('D:/Рабочий стол/Учёба 4й курс 2023/Сетевые/1 лаба - работа с SQLite/Lab_01 IDZ/booking.db','r', encoding ='utf-8-sig')


damp = f_damp.read()
f_damp.close()
con.executescript(damp)

con.commit()
cursor = con.cursor()

cursor.execute('''
DROP TABLE IF EXISTS bill;
''')

cursor.execute('''
CREATE TABLE bill AS
SELECT type_room_name || ' ' || room_name || ' ' || check_in_date || ' / ' || check_out_date 
    AS 'Тип номера и его название, дата заселения и дата выселения', 
    SUM(type_room.price * CAST((julianday(check_out_date) - julianday(check_in_date)) AS INTEGER)) 
    AS 'Стоимость проживания', 
    GROUP_CONCAT(DISTINCT service_name || ' ' || service_start_date) 
    AS 'Название услуги, дата ее получения', SUM(service_booking.price) AS 'Общая оплата за услуги', 
    SUM(type_room.price * CAST((julianday(check_out_date) - julianday(check_in_date)) AS INTEGER) + type_room.price) AS 'Итого'
FROM guest, room_booking, room, type_room, service_booking, service
WHERE guest.guest_name = "Садиев С.И."
    AND room_booking.guest_id = 10
    AND room_booking.check_in_date = "2020-11-04"
    AND room.room_id = 31
    AND type_room.type_room_id = room.type_room_id
    AND service_booking.room_booking_id = 24
    AND service_booking.service_id = service.service_id
GROUP BY type_room_name || ' ' || room_name || ' ' || check_in_date || ' / ' || check_out_date;
''')

cursor.execute('''           
SELECT *
FROM bill
''')
 
print("Тип номера и его название, дата заселения и дата выселения",
      " | Стоимость проживания",
      " | Название услуги, дата ее получения",
      " | Стоимость услуг",
      " | Сумма")

print(cursor.fetchall())

#con.commit() # Наверное применять это к БД не нужно