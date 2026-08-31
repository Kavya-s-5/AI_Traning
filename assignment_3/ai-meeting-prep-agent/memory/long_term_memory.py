import sqlite3


class LongTermMemory:

    def __init__(self, db_path="memory/agent_memory.db"):

        self.connection = sqlite3.connect(db_path)

        self.cursor = self.connection.cursor()

        self.create_table()


    def create_table(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_name TEXT,
                information TEXT
            )
        """)

        self.connection.commit()


    def save_memory(self, client_name, information):

        self.cursor.execute("""
            INSERT INTO memories (client_name, information)
            VALUES (?, ?)
        """, (client_name, information))

        self.connection.commit()


    def get_memories(self, client_name):

        self.cursor.execute("""
            SELECT information
            FROM memories
            WHERE client_name = ?
        """, (client_name,))

        results = self.cursor.fetchall()

        memories = [
            row[0]
            for row in results
        ]

        return memories