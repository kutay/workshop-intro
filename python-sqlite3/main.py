import sqlite3

from sqlite3 import Error

# https://www.sqlitetutorial.net/sqlite-python/

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_messages(conn):
    """
    Query all rows in the messages table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM messages")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_messages_by_user(conn, user_id):
    """
    Query messages by user_id
    :param conn: the Connection object
    :param user_id:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM messages WHERE user_id=?", (user_id,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"sqlite.db"

    conn = create_connection(database)

    with conn:
        print("1. Query messages by user:")
        select_messages_by_user(conn, 1)

        print("2. Query all messages")
        select_all_messages(conn)

        print("3. Post a message")
        # FIXME

main()
