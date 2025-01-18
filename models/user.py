from services.authentications import register, login, logout


class User:
    def __init__(self, name: str, age: int, username: str, password: str) -> None:
        self.name = name
        self.age = age
        self.username = username
        self.password = password
        
    def register(self):
        return register(self.name, self.age, self.username, self.password)
    
    def login(self):
        return login(self.username, self.password)

    def logout(self):
        return logout(self.username)
