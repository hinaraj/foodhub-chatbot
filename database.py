
from langchain_community.utilities import SQLDatabase

# Database path
DB_PATH = "sqlite:///customer_orders.db"

# Load SQLite database
db = SQLDatabase.from_uri(DB_PATH)

def get_database():
    return db
