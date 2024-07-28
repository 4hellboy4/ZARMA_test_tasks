import sqlite3


def fetch_users() -> None:
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()

    query: str = "SELECT name, age FROM users WHERE age > 30"
    cursor.execute(query)
    users: list = cursor.fetchall()

    for user in users:
        print(f"Name: {user[0]}, Age: {user[1]}")

    cursor.close()
    connection.close()


def main() -> None:
    fetch_users()


if __name__ == '__main__':
    main()
