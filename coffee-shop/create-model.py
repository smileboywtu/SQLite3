# use the build in data base SQLite
# use the Python 3.5 as default

# import
import sqlite3

def create_table(db_name, table_name, sql):
	"use to create the entity"
	with sqlite3.connect(db_name) as db:
		cursor = db.cursor()
		cursor.execute("SELECT name FROM sqlite_master WHERE name=?", (table_name,))
		result = cursor.fetchall()
		keep_table = True
		if len(result) == 1:
			response = input("The table {0} already exists, do you wish to recreate it (y/n): ".format(table_name))
			if response.lower() == 'y':
				keep_table = False
				print("The {0} table will be recreated - all existing data will be lost!".format(table_name))
				cursor.execute("DROP TABLE IF EXISTS {0}".format(table_name))
				db.commit()
		else:
			keep_table = False

		if not keep_table:
			cursor.execute(sql)
			db.commit()


if __name__ == "__main__":
		db_name = "coffee_shop.db"
		table_name = "Product"
		sql = """

				CREATE TABLE Product(
					ProductID integer,
					Name text,
					Price real,
					Primary Key(ProductID))

		"""

		create_table(db_name, table_name, sql)
