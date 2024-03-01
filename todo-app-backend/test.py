<<<<<<< HEAD
import psycopg2
DATABASE_URL = 'postgres://postgres:Jesus002@localhost:5432/todo_app'
try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Connected to database successfully!")
    conn.close()
except Exception as e:
    print(f"Error connecting to database: {e}")


dict = {services:
        
  {todo-app-backend:
    image: todo},

  {todo-app-frontend:
    image: todo},
    
  {db:
    image: postgres}
}
=======
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Connected to database successfully!")
    conn.close()
except Exception as e:
    print(f"Error connecting to database: {e}")
>>>>>>> b3af0c27a90eb1209867628a807ce32fd43e287d
