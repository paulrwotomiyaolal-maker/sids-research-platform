from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///research.db"

engine = create_engine(DATABASE_URL)

if __name__ == "__main__":
    conn = engine.connect()
    print("Database initialized.")
    conn.close()