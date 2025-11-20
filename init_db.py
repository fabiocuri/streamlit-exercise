from postgresql_script import get_connection
import psycopg2

def create_tables():
    """Create the necessary tables for the Streamlit app."""
    conn = get_connection()
    if not conn:
        print("Failed to connect to database")
        return False

    try:
        cursor = conn.cursor()

        # Create personal_info table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS personal_info (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create feedback table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id SERIAL PRIMARY KEY,
                rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
                category VARCHAR(100) NOT NULL,
                comments TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()
        print("Tables created successfully!")

        cursor.close()
        conn.close()
        return True

    except psycopg2.Error as e:
        print(f"Error creating tables: {e}")
        if conn:
            conn.rollback()
            conn.close()
        return False

if __name__ == "__main__":
    create_tables()