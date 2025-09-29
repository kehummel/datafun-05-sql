import sqlite3
import pathlib

from loguru import logger

def run_sql_file(connection, file_path):
    
    try: 
        with open(file_path, 'r') as file:
            sql_file: str = file.read()
        with connection:
            connection.executescript(sql_file)
            logger.info(f'Executed: {file_path}')
    except Exception as e:
        logger.error(f'Failed to Execute {file_path}: {e}')
        raise


def main():

    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    SQL_CREATE_FOLDER = ROOT_DIR.joinpath("sql_features")
    DATA_FOLDER = ROOT_DIR.joinpath("Data")
    DB_PATH = DATA_FOLDER.joinpath('datafun_05db.db')

    try:
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to database: {DB_PATH}")

        run_sql_file(connection, SQL_CREATE_FOLDER.joinpath('update_records.sql'))
        run_sql_file(connection, SQL_CREATE_FOLDER.joinpath('delete_records.sql'))

        logger.info("Database setup completed successfully.")
    except Exception as e:
        logger.error(f"Error during database setup: {e}")
    finally:
        connection.close()
        logger.info("Database connection closed.")


if __name__ == '__main__':
    main()