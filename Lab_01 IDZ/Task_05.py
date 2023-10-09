import sqlite3
import pandas as pd # Импортирую библиотеку pandas, для вывода таблиц запросов

# Убираю ограничения по количеству строк в таблице
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

con = sqlite3.connect("booking_py_01.sqlite")
str_way = 'D:/Рабочий стол/Учёба 4й курс 2023/Сетевые/1 лаба - работа с SQLite/Lab_01 IDZ/booking.db'
f_damp = open(str_way,'r', encoding ='utf-8-sig')

damp = f_damp.read()
f_damp.close()
con.executescript(damp)
conn = sqlite3.connect("booking_py_01.sqlite")

con.commit()
cursor = con.cursor()

cursor.execute('''
    DROP TABLE IF EXISTS lll;
''')

# Для каждой комнаты, для списка гостей, которые в ней жили, проставляю им рейтинг по номеру, ориентируясь на дату
cursor.execute('''
    CREATE TABLE lll AS
    SELECT room_id, guest_id, check_in_date, 
        RANK() OVER(PARTITION BY room_id ORDER BY check_in_date) AS order_number
    FROM room_booking   
''')

df = pd.read_sql('''
    SELECT *
    FROM lll
''', conn)

cursor.execute('''
    DROP TABLE IF EXISTS SSS;
''')

# Создаю общий ранг для комнаты - как сумму ранга всех живших в неё гостей
cursor.execute('''
    CREATE TABLE SSS AS
    SELECT room_id, SUM(order_number) AS total_rank
    FROM lll
    GROUP BY room_id;
''')

cursor.execute('''
    DROP TABLE IF EXISTS WWW;
''')

# Назначаю для каждого гостя ранг - его порядковый номер / общий ранг комнаты
cursor.execute('''
    CREATE TABLE WWW AS
    SELECT lll.room_id, guest_id, check_in_date, order_number, total_rank, ROUND(CAST(order_number AS FLOAT) / CAST(total_rank AS FLOAT), 2) AS rung_guest
    FROM lll, SSS
    WHERE lll.room_id = sss.room_id
''')

df = pd.read_sql('''
    SELECT *
    FROM WWW
''', conn)

print(df)

# Для всех гостей, суммирую их ранги, и вывожу в порядке убывания рангов
df = pd.read_sql('''
    SELECT guest.guest_name, SUM(rung_guest) AS rang_guest
    FROM WWW, guest
    WHERE WWW.guest_id = guest.guest_id
    GROUP BY guest_name
    ORDER BY rang_guest DESC;
''', conn)

print(df)