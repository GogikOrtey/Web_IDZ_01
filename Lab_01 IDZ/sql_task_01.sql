-- SELECT * 
-- SELECT room.room_name AS "Номер", 
--     type_room.type_room_name AS "Тип номера", 
--     type_room.price AS "Цена"
-- FROM room, type_room
-- WHERE room.room_id = type_room.type_room_id 

SELECT room.room_name AS "Номер", 
    type_room.type_room_name AS "Тип номера", 
    type_room.price AS "Цена"
FROM room
JOIN type_room ON room.room_id = type_room.type_room_id 
WHERE (CONVERT(INT, SUBSTRING(room.room_name, LEN(room.room_name))) % 2) = 1





