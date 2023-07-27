import sqlite3

def login(username, password):
    # This code is vulnerable to SQL injection
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(username, password)
    cursor.execute(query)

    user = cursor.fetchone()
    cursor.close()
    conn.close()

    return user

if __name__ == "__main__":
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user = login(username, password)

    if user:
        print("Login successful. Welcome, " + user[1])
    else:
        print("Login failed. Invalid username or password.")
