from sqlalchemy import create_engine
from sqlalchemy import inspect

# Replace this with your actual database URL
DATABASE_URL = "postgresql://postgres:37472396@localhost/letsgomff"

# Create an engine to connect to the database
engine = create_engine(DATABASE_URL)

# Inspect the database
inspector = inspect(engine)

# Get all table names
tables = inspector.get_table_names()

# Print the tables
print("Tables in the database:")
for table in tables:
    print(table)
