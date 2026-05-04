# Simple authentication simulation

users = []

def register(username, email, password):
    user = {
        "username": username,
        "email": email,
        "password": password
    }
    users.append(user)
    print(f"User {username} registered successfully")


def login(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"Welcome {username}")
            return user   # IMPORTANT CHANGE
    print("Invalid credentials")
    return None
