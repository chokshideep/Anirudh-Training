from sqlalchemy import create_engine, text
import urllib

# Replace with your actual connection string details
username = "deep"
password = "training@123"
server = "sr-training.database.windows.net"
database = "db-training"
driver = "ODBC Driver 18 for SQL Server"

# Construct the connection URL
params = urllib.parse.quote_plus(
    f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"


def test_connection():
    try:
        # Create an engine instance
        engine = create_engine(DATABASE_URL)

        # Connect to the database
        with engine.connect() as connection:
            # Execute a simple query
            result = connection.execute(text("SELECT 1"))
            for row in result:
                print("Connection successful, query result:", row)
        print("Database connection tested successfully.")
    except Exception as e:
        print("Error testing database connection:", str(e))


if __name__ == "__main__":
    test_connection()
