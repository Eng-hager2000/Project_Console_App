from models.user import User
from uses.file_operations import *
import json

class AuthController:

    users_filename = 'data/users.json'
    
    def register(self, first_name, last_name, email, password, mobile_phone):
        new_user = User(first_name, last_name, email, password, mobile_phone)
        status = new_user.save()
        return new_user
    
    def login(self, email, password):
        user = User.find_by_email(email)
        if user and user.check_password(password):
            return user
        return None
    
    def is_email_unique(self, email):
        user = User.find_by_email(email)
        if user:
            return False
        return True

