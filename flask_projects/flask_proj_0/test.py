class User:
    def __init__(self):
        self.name="Ashis Babu Maharjan"
        self.is_logged_in=False

def authenticate_user(func):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in:
            return func(*args,**kwargs)
        else:
            return "Sorry authentication failed!!"
    return wrapper

@authenticate_user
def welcome_dashboard(user_obj):
    return f'User {user_obj.name} is logged in successfully.'



user=User()
user.is_logged_in=True
message=welcome_dashboard(user)
print(message)

