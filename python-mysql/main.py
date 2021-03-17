import mysql.connector

from mysql.connector import errorcode

def create_tables(cursor):

    try:
        query = "CREATE TABLE `users` (`user_id` int(11) NOT NULL AUTO_INCREMENT, `name` varchar(16) NOT NULL, PRIMARY KEY (`user_id`)) ENGINE=InnoDB"
        cursor.execute(query)
    except mysql.connector.Error as err:
        print("Failed creating table: {}".format(err))
        # exit(1)


def insert_data(cursor):
    add_user = ("INSERT INTO users (name) VALUES (%s)")
    data_user = ('aykut')

    cursor.execute(add_user, (data_user,))


def main():
    cnx = mysql.connector.connect(user='root',
                                  password='my-secret-pw',
                                  host='127.0.0.1',
                                  database='employees')
    cursor = cnx.cursor()

    create_tables(cursor)
    insert_data(cursor)

    query = ("SELECT * FROM users")
    cursor.execute(query)

    for (name) in cursor:
        print("{}".format(name))

    cnx.close()


main()
