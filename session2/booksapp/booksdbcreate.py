import sqlite3


def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        print('database %s successfully created' % db_file)
        return connection
    except sqlite3.Error as error:
        print(error)
        return None


def create_table_authors(c, sql):
    if c:
        cursor = c.cursor()
        try:
            cursor.execute(sql)
            print('table authors created')
        except sqlite3.Error as error:
            print(error)
    else:
        print('No connection')


def create_table_books(c, sql):
    if c:
        cursor = c.cursor()
        try:
            cursor.execute(sql)
            print('table books created')
        except sqlite3.Error as error:
            print(error)
    else:
        print('No connection')


def create_table_categories(c, sql):
    if c:
        cursor = c.cursor()
        try:
            cursor.execute(sql)
            print('table categories created')
        except sqlite3.Error as error:
            print(error)
    else:
        print('no connection')


def main():
    connection = create_connection('booksappdb.db')

    sql_authors_creation = '''
        CREATE TABLE 'authors' 
        ('id' INTEGER NOT NULL, 
        'name' TEXT NOT NULL, 
        'gender' TEXT NOT NULL, 
        PRIMARY KEY('id'))
    '''

    sql_books_creation = '''
            CREATE TABLE 'books' 
            ('id' INTEGER NOT NULL, 
            'title' TEXT NOT NULL, 
            'author_id' INTEGER NOT NULL, 
            'category_id' INTEGER NOT NULL, 
            PRIMARY KEY('id'))
        '''

    sql_categories_creation = '''
                CREATE TABLE 'categories' 
                ('id' INTEGER NOT NULL, 
                'name' TEXT NOT NULL, 
                PRIMARY KEY('id'))
            '''

    if connection:
        create_table_authors(connection, sql_authors_creation)
        create_table_books(connection, sql_books_creation)
        create_table_categories(connection, sql_categories_creation)

    else:
        print('connection not available')


if __name__ == '__main__':
    main()