class Room:

    def __init__(self, number: int, size: int, price: float, type: str, available: bool):
        self.number = number
        self.size = size
        self.price = price
        self.type = type
        self.is_available = available

    def book(self):
        self.is_available = False
    
    def mark_available(self):
        self.is_available = True
    
    def room_info(self):
        return self.number, self.size, self.price, self.type, self.is_available