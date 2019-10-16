import sqlite3


def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        print('database %s successfully created' % db_file)
        return connection
    except sqlite3.Error as error:
        print(error)
        return None


def insert_author(c, sql):
    if c:
        cursor = c.cursor()
        try:
            cursor.execute(sql)
            c.commit()
            return cursor.lastrowid
        except sqlite3.Error as error:
            print(error)
    else:
        print('no connection')


def main():
    connection = create_connection('booksappdb.db')

    insert_sql = '''
        INSERT INTO authors (name, gender) VALUES ('John Doe', 'm')
    '''

    if connection:
        new_author = insert_author(connection, insert_sql)
        print('id %s has been created' % new_author)
    else:
        print('no connection')


if __name__ == '__main__':
    main()