-- SELECT DISTINCT * 
-- FROM room_booking
-- WHERE status_id = 1

-- Мне нужно получить фамилию (или ФИО) гостя, по его id

SELECT DISTINCT guest.guest_name, type_room_name --*, guest.guest_id
FROM room_booking, room, type_room, guest
WHERE status_id = 1 
    AND guest.guest_id = 8
    AND room.room_id = room_booking.room_id
    AND room.type_room_id = type_room.type_room_id
    AND room_booking.guest_id = guest.guest_id