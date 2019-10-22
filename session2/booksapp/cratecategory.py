import sqlite3


def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        print('database %s successfully created' % db_file)
        return connection
    except sqlite3.Error as error:
        print(error)
        return None


def insert_category(c, sql):
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
        INSERT INTO categories (name) VALUES ('{0}')
    '''

    if connection:
        name = input('Enter the category name: ')
        new_category = insert_category(connection, insert_sql.format(name))
        print('id %s has been created' % new_category)
    else:
        print('no connection')


if __name__ == '__main__':
    main()