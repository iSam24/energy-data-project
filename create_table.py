import psycopg2
from psycopg2 import sql
from config import DB_HOST, DB_NAME, DB_USER, DB_PASS, DB_PORT


connection = None

try:
    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    cursor = connection.cursor()
    
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS test_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    '''
    print("Table created successfully!")
    
except Exception as error:
    print(f"Error occurred: {error}")
    
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed.")
