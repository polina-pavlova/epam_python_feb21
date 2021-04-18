import sqlite3


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.database_name)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def __len__(self):
        self.cursor.execute(f"SELECT COUNT(*) from {self.table_name}")
        return self.cursor.fetchone()[0]

    def __contains__(self, item):
        self.cursor.execute(
            f"SELECT * from {self.table_name} WHERE name=:item", {"item": item}
        )
        return self.cursor.fetchone()

    def __getitem__(self, item):
        self.cursor.execute(
            f"SELECT * from {self.table_name} WHERE name=:item", {"item": item}
        )
        return tuple(self.cursor.fetchone())

    def __iter__(self):
        yield from self.cursor.execute(f"SELECT * from {self.table_name}")

    def close_connection(self):
        self.connection.cursor().close()
        self.connection.close()
