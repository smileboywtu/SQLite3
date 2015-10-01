# select the data using the like API
# use the python 3.5 as default

import sqlite3

def select_data(db_name, table_name, condition):
    "find all the data with the same kind"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT title, releaseYear FROM {0} WHERE title LIKE ?".format(table_name), (condition,))
        result = cursor.fetchall()
        return result

def select_from_multi(db_name, table_name, conditon):
    "select from multiple tables"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT title, genreName FROM {0}, {1} WHERE title=? AND genreName IN (?,?)".format(table_name[0], table_name[1]), (condition[0], condition[1], condition[2]))
        result = cursor.fetchall()
        return result

if __name__ == '__main__':

    db_name = "movie.db"
    table_name = "film"
    condition = "Die Hard%"

    result = select_data(db_name, table_name, condition)
    print(result)

    table_name = ("film", "genre")
    condition = ("Die Hard", "Action", "Thriller")
    result = select_from_multi(db_name, table_name, condition)
    print(result)
