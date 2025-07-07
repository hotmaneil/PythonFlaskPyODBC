import pyodbc

def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost,1433;"
        "DATABASE=DB_ADAPTER_STANDARD;"
        "UID=sa;"
        "PWD=Sunsda;"
        "TrustServerCertificate=yes;"
    )