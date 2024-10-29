from sqlalchemy import create_engine


DATABASE_URI = 'mysql+pymysql://root:843RnR$$@localhost:3306/bakery_db'

try:
  
    engine = create_engine(DATABASE_URI)

    connection = engine.connect()
    print("Connection successful!")
    connection.close()
except Exception as e:
    print("Connection failed:", e)
