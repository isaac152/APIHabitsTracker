from werkzeug.security import generate_password_hash, check_password_hash
class User:
    username:str
    name:str
    password:str

    def __init__(self,username,password,name=''):
        self.username=username
        self.name=name
        self._password=password
        self.set_password(password)

    def set_password(self,password):
        self.password = generate_password_hash(password)
    
    def change_password(self, old_password,new_password):
        if(self.check_password(old_password)):
            self.set_password(new_password)
            return True
        return False
    def set_username(self, username):
        self.username = username

    def set_name(self,name):
        self.name=name

    def check_password(self, password)->bool:
        return check_password_hash(password,self._password)

    def __str__(self):
        return f"{self.username}"
