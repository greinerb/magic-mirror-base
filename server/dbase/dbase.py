import sqlite3

class dbase:
    def __init__(self):
        self._dbpath = 'res/db/mirror.db' # Database file path
        self.setup()

    # Connect to database
    def connect(self):
        self._cn = sqlite3.connect(self._dbpath) # Created Database "connection"
        self._db = self._cn.cursor() # Databse Cursor

    # Querry Database
    def qry(self, qry):
        self.connect()
        dat = self.exe(qry)
        self.close()

        return dat

    # Only execute querry
    def exe(self, qry):
        self._db.execute(qry)
        return self._db.fetchall()

    # Commit changes and close
    def close(self):
        self._cn.commit()
        self._cn.close()

    #TODO: Add Setup method to initate all of the tables
    def setup(self):
        self.connect()

        # Create a basic weather test table
        self.exe("""
            CREATE TABLE IF NOT EXISTS test (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                temperature INTEGER NOT NULL,
                icon TEXT NOT NULL
            )
            """)

        self.close()

# Initiate database instance
db = dbase()
