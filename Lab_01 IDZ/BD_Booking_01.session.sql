-- SELECT room.room_id, room.room_name, room.type_room_id, type_room.type_room_name, COUNT(room_booking.guest_id) AS guest_count
-- FROM room, room_booking, type_room
-- WHERE room.room_id = room_booking.room_id
--     AND type_room.type_room_id = room.type_room_id
-- GROUP BY room.room_id, room.room_name, room.type_room_id, type_room.type_room_name;

-- SELECT room.room_id, room.room_name, room.type_room_id, type_room.type_room_name, COUNT(room_booking.guest_id) AS guest_count
-- FROM room
-- JOIN room_booking ON room.room_id = room_booking.room_id
-- JOIN type_room ON type_room.type_room_id = room.type_room_id
-- GROUP BY room.room_id, room.room_name, room.type_room_id, type_room.type_room_name;

-- SELECT room.room_id, room.room_name, room.type_room_id, type_room.type_room_name, COUNT(room_booking.guest_id)
-- FROM room, room_booking, type_room
-- WHERE room.room_id = room_booking.room_id
--     AND type_room.type_room_id = room.type_room_id
-- GROUP BY room.room_id, room.room_name, room.type_room_id, type_room.type_room_name;



SELECT room.room_id, room.room_name, room.type_room_id, COUNT(room_booking.guest_id) AS guest_count
FROM room
JOIN room_booking ON room.room_id = room_booking.room_id
GROUP BY room.room_id, room.room_name, room.type_room_id

-- room_booking.status_id = 2

-- -- Запрос готов

-- Вывести номера, группировка по типу, room_booking статус "Забронирован"

-- SELECT room.room_id, room.room_name, type_room.type_room_id, type_room.type_room_name, room_booking.status_id, status_name
-- FROM room, room_booking, status, type_room
-- WHERE room.room_id = room_booking.room_booking_id 
--     AND room_booking.status_id = status.status_id
--     AND type_room.type_room_id = room.type_room_id


-- SELECT room.room_id, room.room_name, room_booking.status_id, status_name
-- FROM room, room_booking, status
-- WHERE room.room_id = room_booking.room_booking_id 
--     AND room_booking.status_id = status.status_id

