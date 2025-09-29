import sqlite3
import pathlib
import pandas as pd
import matplotlib.pyplot as plt 

from loguru import logger

def run_sql_file(connection, file_path) -> None:
    """
    Executes a SQL file using the provided SQLite connection.

    Args:
        connection (sqlite3.Connection): SQLite connection object.
        file_path (str): Path to the SQL file to be executed.
    """
    try:
        with open(file_path, 'r') as file:
            sql_script: str = file.read()
        with connection:
            connection.executescript(sql_script)
            logger.info(f"Executed: {file_path}")
    except Exception as e:
        logger.error(f"Failed to execute {file_path}: {e}")
        raise

def run_sql_file_to_df(conn: sqlite3.Connection, file_path) -> pd.DataFrame:
    """Read SQL file and return a DataFrame."""
    with open(file_path, 'r') as file:
        sql_query = file.read()
    return pd.read_sql_query(sql_query, conn)

def run_to_df(conn: sqlite3.Connection, sql: str) -> pd.DataFrame:
    """Execute SQL string and return a DataFrame."""
    return pd.read_sql_query(sql, conn)

def create_scatter_plot(conn: sqlite3.Connection, sql_file_path):
    """Create scatter plot from SQL file query results."""
    df = run_sql_file_to_df(conn, sql_file_path)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(df['age_when_published'], df['year_published'])
    plt.xlabel('The Age of Author When Published')
    plt.ylabel('Year their book was Published')
    plt.title('Year Published vs Age of Author')
    plt.grid(True, alpha=0.3)
    plt.show()

def main():

    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    SQL_CREATE_FOLDER = ROOT_DIR.joinpath("sql_queries")
    DATA_FOLDER = ROOT_DIR.joinpath("Data")
    DB_PATH = DATA_FOLDER.joinpath('datafun_05db.db')

    try:
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to database: {DB_PATH}")

        # Execute SQL file (for CREATE, INSERT, UPDATE, etc.)
        run_sql_file(connection, SQL_CREATE_FOLDER.joinpath('query_join.sql'))
        df_join = run_to_df(connection, "SELECT * FROM authors_books LIMIT 10")
        logger.info(f"authors_books table has data: {len(df_join)} rows shown")
        
        # Execute SQL files and get DataFrames
        df_sorting = run_sql_file_to_df(connection, SQL_CREATE_FOLDER.joinpath('query_sorting.sql'))
        logger.info(f"Sorting query returned {len(df_sorting)} rows")
        
        df_group_by = run_sql_file_to_df(connection, SQL_CREATE_FOLDER.joinpath('query_group_by.sql'))
        logger.info(f"Group by query returned {len(df_group_by)} rows")
        
        df_filter = run_sql_file_to_df(connection, SQL_CREATE_FOLDER.joinpath('query_filter.sql'))
        logger.info(f"Filter query returned {len(df_filter)} rows")
        
        # Create scatter plot from aggregation query
        create_scatter_plot(connection, SQL_CREATE_FOLDER.joinpath('query_aggregation.sql'))

        logger.info("Database operations completed successfully.")
    except Exception as e:
        logger.error(f"Error during database operations: {e}")
    finally:
        connection.close()
        logger.info("Database connection closed.")


if __name__ == '__main__':
    main()