import sqlite3


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def connect_db(self):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            return cursor

    def __len__(self):
        cursor = self.connect_db()
        cursor.execute(f"SELECT COUNT(*) from {self.table_name}")
        return cursor.fetchone()[0]

    def __contains__(self, item):
        cursor = self.connect_db()
        cursor.execute(
            f"SELECT * from {self.table_name} WHERE name=:item", {"item": item}
        )
        return cursor.fetchone()

    def __getitem__(self, item):
        cursor = self.connect_db()
        cursor.execute(
            f"SELECT * from {self.table_name} WHERE name=:item", {"item": item}
        )
        return cursor.fetchone()

    def __iter__(self):
        cursor = self.connect_db()
        cursor.execute(f"SELECT * from {self.table_name}")
        return cursor
