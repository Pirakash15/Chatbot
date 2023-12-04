import sqlite3

class ChatDatabase:
    def __init__(self, db_path="chatbot.db"):
        self.db_path = db_path
        self.conn = None

    def _connect(self):
        return sqlite3.connect(self.db_path)
            
    def create_tables(self):
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sender TEXT NOT NULL,
                    content TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

    def insert_message(self, sender, content):
        with self._connect() as conn:
            conn.execute("INSERT INTO messages (sender, content) VALUES (?, ?)", (sender, content))

    def get_all_messages(self):
        with self._connect() as conn:
            cursor = conn.execute("SELECT sender, content, timestamp FROM messages ORDER BY timestamp ASC")
            return cursor.fetchall()

    def clear_messages(self):
        with self._connect() as conn:
            conn.execute("DELETE FROM messages")

    def close(self):
        if self.conn:
            self.conn.close()

    def __enter__(self):
        self.conn = self._connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()
