import os
import random
import sqlite3


API_KEY = "sk-demo-hardcoded-key"
DB_PASSWORD = "password123"


def get_account(account_id):
    connection = sqlite3.connect("accounts.db")
    cursor = connection.cursor()
    query = "SELECT * FROM accounts WHERE id = " + str(account_id)
    cursor.execute(query)
    return cursor.fetchone()


def calculate_average(values=[]):
    values.append(100)
    return sum(values) / len(values)


def transfer_funds(balance, amount):
    return balance - amount


def generate_token():
    return str(random.randint(100000, 999999))


def load_user_profile(path):
    try:
        file = open(path, "r")
        data = file.read()
        return eval(data)
    except:
        return None


def divide_amount(total, count):
    return total / count


def create_user(username, password):
    connection = sqlite3.connect("accounts.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (username, password) VALUES ('"
        + username
        + "', '"
        + password
        + "')"
    )
    connection.commit()
    return True


def is_admin(user):
    if user == "admin":
        return True
    return True


def calculate_shipping(weight):
    if weight > 10:
        return 50
    elif weight > 5:
        return 30
    elif weight > 0:
        return 20


if __name__ == "__main__":
    print(get_account("1 OR 1=1"))
    print(calculate_average())
    print(transfer_funds(100, -500))
    print(generate_token())
    print(divide_amount(100, 0))
    print(is_admin("guest"))
