from .user import User
from .room import Room


class Book:
    def __init__(self, user: User, room: Room):
        self.user = user
        self.room = room
    
    def book_room(self):
        if self.room.is_available:
            self.room.book()
            return f"{self.room.number} is successfully booked for {self.user.name}"
        else:
            return f"{self.room.number} is not available!!!"
    
    def mark_as_available(self):
        self.room.mark_available()
        return f"{self.room.room_info()} is available now!"