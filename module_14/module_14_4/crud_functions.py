import sqlite3

connection = sqlite3.connect("products.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Products(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                price INTEGER NOT NULL
            )
        """
    )
    connection.commit()


def add_product(title, description, price):
    cursor.execute(
        """
            INSERT INTO Products (title, description, price) VALUES(?, ?, ?)
        """,
        (title, description, price),
    )
    connection.commit()


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    data = cursor.fetchall()
    connection.close()
    return data


# initiate_db()
#
# add_product("Пингвин", "С ребрышками", 150)
# add_product("Пингвин", "Зелёный", 120)
# add_product("Пингвин", "Чёрный", 100)
# add_product("Пингвин", "Dart Penguin", 200)
#
# for prod in get_all_products():
#     print(prod)
connection.commit()
if __name__ == '__main__':
    # connection.commit()
    connection.close()
