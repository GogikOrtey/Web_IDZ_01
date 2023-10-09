-- Садиев С.И., проживающий в номере С-0226 с 4 ноября 2020

-- Создать новую таблицу bill

-- Тип номера
-- Навзание номера
-- Дату заселения и выселения
-- Цена проживания за день

-- --SELECT *
-- SELECT type_room_name, room_name, check_in_date, check_out_date, type_room.price
-- FROM guest, room_booking, room, type_room
-- WHERE guest.guest_name = "Садиев С.И."
--     AND room_booking.guest_id = 10
--     AND room_booking.check_in_date = "2020-11-04"
--     AND room.room_id = 31
--     AND type_room.type_room_id = room.type_room_id

-- -- Запрос готов

-- DROP TABLE IF EXISTS bill;

-- CREATE TABLE bill ( 
--     guest_name VARCHAR(255), 
--     room_type VARCHAR(255), 
--     room_name VARCHAR(255), 
--     check_in_out_date VARCHAR(255), 
--     total_cost_booking DECIMAL(10,2),

--     service_name VARCHAR(255),
--     service_dates TEXT,
--     total_cost_service DECIMAL(10,2)
-- );

-- INSERT INTO bill (guest_name, room_type, room_name, check_in_out_date, total_cost) 
-- SELECT 'Садиев С.И.' AS guest_name, 
--     type_room.type_room_name AS room_type, 
--     room.room_name AS room_name, 
--     room_booking.check_in_date ||
--     ' / ' ||
--     room_booking.check_out_date AS check_in_out_date, 
--     (julianday(room_booking.check_out_date) - julianday(room_booking.check_in_date)) * type_room.price AS total_cost 
-- FROM guest 
-- JOIN room_booking ON guest.guest_id = room_booking.guest_id 
-- JOIN room ON room_booking.room_id = room.room_id 
-- JOIN type_room ON room.type_room_id = type_room.type_room_id
-- WHERE guest.guest_name = 'Садиев С.И.' 
--     AND room.room_name = 'С-0226' 
--     AND room_booking.check_in_date = '2020-11-04';



-- Посчитать стоимость проживания за все дни

-- Название услуги
-- Дата получения услуги (м/б несколько дат)
-- Стоимость услуги

--SELECT *
-- SELECT service_name, service_start_date, price
-- FROM service_booking, service
-- WHERE room_booking_id = 24
--     AND service_booking.service_id = service.service_id

-- -- INSERT INTO bill (service_name, service_dates, total_cost_service)
-- -- SELECT service.service_name,
-- --        GROUP_CONCAT(service_booking.service_start_date, ', ') AS service_dates,
-- --        SUM(price) AS total_cost_service
-- -- FROM guest
-- -- JOIN room_booking ON room.room_id = room_booking.room_id
-- -- JOIN service_booking ON room_booking.room_booking_id = service_booking.room_booking_id
-- -- JOIN service ON service_booking.service_id = service.service_id
-- -- WHERE guest.guest_name = 'Садиев С.И.'
-- --   AND room.room_name = 'С-0226'
-- --   AND room_booking.check_in_date = '2020-11-04'
-- -- GROUP BY service.service_name;

-- Посчитать сумму за кол-во услуг

-- Посчиать всю сумму (Итого)

-- SELECT *
-- FROM bill

-- Финальный запрос:

DROP TABLE IF EXISTS bill;

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

SELECT *
FROM bill