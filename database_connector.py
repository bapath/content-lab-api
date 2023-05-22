from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.exc import OperationalError
import os

class Database:
    def __init__(self):
        db_conn = os.environ["DB_CONN"]
        engine = None
        metadata = MetaData()

        # Create the database engine
        try:
            engine = create_engine(db_conn)
            metadata.bind = engine
            engine.connect()
            print("connection succesful")
        except OperationalError as e:
            raise e

        # Get the inspector object for the engine
        self.inspector = inspect(engine)

    def get_table_names(self):
        # Get the names of all tables
        table_names = self.inspector.get_table_names()
        return table_names

    def get_column_names(self,table_name):
        # Get the names of all tables
        column_names = [column["name"] for column in self.inspector.get_columns(table_name)]
        return column_names
