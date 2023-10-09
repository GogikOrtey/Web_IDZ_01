-- Для каждой комнаты выводит список гостей, которые в ней жили, проставляя им рейтинг по номеру, ориентируясь на дату

-- SELECT room_id, guest_id, check_in_date,
--        ROW_NUMBER() OVER(PARTITION BY room_id ORDER BY check_in_date) AS order_number
-- FROM room_booking

-- То-же самое, но с использованием RANK()

-- SELECT room_id, guest_id, check_in_date, RANK() OVER(PARTITION BY room_id ORDER BY check_in_date) AS order_number
-- FROM room_booking

--DROP TABLE IF EXISTS lll;

-- CREATE TABLE lll AS
-- SELECT room_id, guest_id, check_in_date, RANK() OVER(PARTITION BY room_id ORDER BY check_in_date) AS order_number
-- FROM room_booking

-- SELECT *
-- FROM lll

SELECT room_id, guest_id, check_in_date, order_number, SUM(order_number) AS total_order_number
FROM lll
GROUP BY room_id, guest_id, check_in_date, order_number;

SELECT room_id, SUM(order_number) AS total_order_number
FROM lll
GROUP BY room_id;



-- SELECT room_id, SUM(RANK() OVER(PARTITION BY room_id ORDER BY check_in_date)) AS total_rank
-- FROM room_booking
-- GROUP BY room_id;

