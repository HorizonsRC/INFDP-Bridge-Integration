import pyodbc
import logging
import sys

# This class handles the connection to the server
# I will properly document and comment all the functions later.
# I feel the docstrings and function names make it self explanatory

class ODBCHandler:
    def __init__(self, server, driver, database):
        """
        Initialize the ODBCHandler with the specified database connection details.
        
        Args:
            server (str): The server address.
            driver (str): The ODBC driver to use.
            database (str): The name of the database.
        """
        logging.debug(f"Initialising ODBCHandler for '{server}' using '{driver}'")
        self.server = server
        self.driver = driver
        self.database = database
        self.auto_commit = True
        logging.debug(f"Available drivers: {pyodbc.drivers()}")

        try:
            conn = pyodbc.connect(driver = driver,
                                  server = server,
                                  database = database,
                                  trusted_connection = "Yes")
            self.cursor = conn.cursor()
            logging.info(f"Connection to ODBC database '{server}' established.")

        except pyodbc.Error as e:
            logging.exception(f"Connection to ODBC database failed! {e}")
            print("Exiting...")
            sys.exit()

    def query(self, query):
        """
        Execute a custom SQL query.

        Args:
            query (str): The SQL query to be executed.
        """
        result = self.cursor.execute(query).fetchall()
        return result

    def select(self, target, table) -> list:
        """
        Perform a SELECT query on the specified table and return the results.
        
        Args:
            target (str): The columns to select in the query.
            table (str): The name of the table.
        
        Returns:
            list: A list containing the query results.
        
        Example: `odbc.select("*", "users")`"""
        try:
            query = f"SELECT {target} FROM {table}"
            result = self.cursor.execute(query).fetchall()
            return result
        except pyodbc.ProgrammingError as e:
            logging.error("Select statement went wrong! {e}")

    def create_table(self, table_name, table_dict):
        """
        Create a new table in the database.

        Args:
            table_name (str): The name of the new table.
            table_dict (str): A dictionary defining the columns and their data types.
        """
        columns = ', '.join([f'{column} {data_type}' for column, data_type in table_dict.items()])
        query = "SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE'"
        table_check = self.cursor.execute(query).fetchall()
        if table_name not in table_check:
            query = f"IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{table_name}' and xtype='U') CREATE TABLE {table_name} ({columns});"
            try:
                self.cursor.execute(query)
                if self.auto_commit:
                    self.cursor.commit()
                logging.info(f"Added '{table_name}' successfully.")
            except pyodbc.Error as e:
                logging.error(f'Error creating table! {e}')
        else:
            logging.warn(f"Table '{table_name}' already exists!")

    def truncate_table(self, table_name):
        """
        Truncate the specified table, removing all rows.

        Args:
            table_name (str): The name of the table to be truncated.
        """
        try:
            self.cursor.execute(f"TRUNCATE TABLE {table_name}")
            if self.auto_commit:
                self.commit()
        except pyodbc.Error as e:
            logging.error(f"Error truncating table! {e}")

    def add_foreign_key(self, table_name, column, referenced_table, referenced_column):
        """
        Add a foreign key to an existing column of a table
    
        Args:
            table_name (str): The name of the table with the column.
            column (str): The column you want to be a foreign key.
            referenced_table (str): The table containing the column you want referenced.
            referenced_column (str): The column of the referenced table that you want to be the target of the foreign key.
        """

        try:
            self.cursor.execute(
                f"ALTER TABLE {table_name} ADD FOREIGN KEY ({column}) REFERENCES {referenced_table}({referenced_column});"
            )
            logging.debug(f"Added foreign key to {column} on {table_name}.")
            if self.auto_commit:
                self.commit()
        except pyodbc.Error as e:
            logging.error(f"Error adding foreign key! {e}")

    def get_all_tables(self) -> list:
        """
        Retrieve a list of all tables in the database.
    
        Returns:
            list: A list containing the names of all base tables in the database.
        """
        query = "SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE'"
        
        try:
            result = self.cursor.execute(query).fetchall()
            table_names = [row.table_name for row in result]
            return table_names
        except pyodbc.Error as e:
            logging.error(f'Error retrieving tables! {e}')
            return None

    def get_columns_of_table(self, table_name) -> list:
        """
        Retrieve the column names of a specific table.
    
        Args:
            table_name (str): The name of the table.
        
        Returns:
            list: A list containing the column names of the specified table.
        """
        query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'"

        try:
            result = self.cursor.execute(query).fetchall()
            column_names = [row.COLUMN_NAME for row in result]
            return column_names
        except pyodbc.Error as e:
            logging.error(f"Error retrieving columns of '{table_name}'! {e}")
            return None

    def insert_into_table(self, table_name, data_list):
        """
        Insert data into a specified table.
    
        Args:
            table_name (str): The name of the table where data will be inserted.
            data_list (dict): A dictionary containing column-value pairs for the data to be inserted.
        """
        columns = ', '.join(data_list.keys())
        values = ', '.join([f"'{value}'" for value in data_list.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        logging.debug(f"Query: {query}")
        try:
            self.cursor.execute(query)
            if self.auto_commit:
                self.commit()
            logging.info(f"Data inserted successfully into '{table_name}'")
            logging.debug(f"Data inserted into table: {values}")
        except pyodbc.Error as e:
            logging.error(f"Error inserting data into '{table_name}'! {e}")

    def drop_table(self, table_name):
        """
        Drop (delete) a specified table from the database.
    
        Args:
            table_name (str): The name of the table to be dropped.
        """
        query = f"DROP TABLE {table_name}"

        try:
            self.cursor.execute(query)
            if self.auto_commit:
                self.commit()
            logging.info(f"Removed '{table_name}' successfully.")
        except pyodbc.Error as e:
            logging.error(f"Error dropping table '{table_name}'! {e}")

    def update_table(self, table_name, update_dict, condition_dict):
        """
        Update data in a specified table based on a given condition.
    
        Args:
            table_name (str): The name of the table to be updated.
            update_dict (dict): A dictionary containing column-value pairs for the update.
            condition_dict (dict): A dictionary specifying the condition for the update.
        """
        set_clause = ', '.join([f"{column} = '{value}'" for column, value in update_dict.items()])
        where_clause = ' AND '.join([f"{column} = '{value}'" for column, value in condition_dict.items()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"

        try:
            self.cursor.execute(query)
            if self.auto_commit:
                self.commit()
            logging.info(f"Data updated successfully in '{table_name}'")
        except pyodbc.Error as e:
            logging.error(f"Error updating data in '{table_name}'! {e}")

    def delete_from_table(self, table_name, condition_dict):
        """
        Delete data from a specified table based on a given condition.
    
        Args:
            table_name (str): The name of the table from which data will be deleted.
            condition_dict (dict): A dictionary specifying the condition for the deletion.
        """

        where_clause = ' AND '.join([f"{column} = '{value}'" for column, value in condition_dict.items()])
        query = f"DELETE FROM {table_name} WHERE {where_clause}"

        try:
            self.cursor.execute(query)
            if self.auto_commit:
                self.commit()
            logging.info(f"Data deleted successfully from '{table_name}'")
        except pyodbc.Error as e:
            logging.error(f"Error deleting data from '{table_name}'! {e}")

    def set_auto_commit(self, bool):
        """
        Set the auto-commit behavior of the database connection.
    
        Args:
            bool (bool): If True, auto-commit is enabled; if False, it is disabled.
        """
        self.auto_commit = bool
        logging.debug(f"Setting 'auto_commit' to {bool}.")

    def set_referential_integrity(self, table_name, bool):
        """
        Set referential integrity (foreign key constraints) on or off for a specified table.
    
        Args:
            table_name (str): The name of the table.
            bool (bool): If True, referential integrity is enabled; if False, it is disabled.
        """
        try:
            if bool:
                logging.debug(f"Setting referential integrity on '{table_name}'")
                self.cursor.execute(f"ALTER TABLE {table_name} WITH CHECK CHECK CONSTRAINT ALL")
            else:
                logging.debug(f"Disabling referential integrity on '{table_name}'")
                self.cursor.execute(f"ALTER TABLE {table_name} NOCHECK CONSTRAINT ALL")
            if self.auto_commit:
                self.commit()
        except pyodbc.Error as e:
            logging.error(f"Error setting referential integrity on '{table_name}' to {bool}! {e}")

    def get_constraint_name(self, table_name, column_name) -> str:
        """
        Retrieve the name of the constraint (foreign key) for a specified table and column.

        Args:
            table_name (str): The name of the table.
            column_name (str): The name of the column.
            
        Returns:
            str: The name of the constraint, or None if not found.
        """

        query = f"""
        SELECT CONSTRAINT_NAME
        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
        WHERE TABLE_NAME = '{table_name}' AND COLUMN_NAME = '{column_name}'
        """
        
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
        except pyodbc.Error as e:
            logging.error(f"Error getting constraint name! {e}")
        finally:
            return result[0] if result else None

    def delete_fk_constraint(self, table_name, column_name):
        """
        Delete a foreign key constraint from a specified table and column.
    
        Args:
            table_name (str): The name of the table.
            column_name (str): The name of the column.
        """
        try:
            constraint_name = self.get_constraint_name(table_name, column_name)
            if constraint_name:
                logging.debug(f"Dropping constraint '{constraint_name}' on '{table_name}'")
                self.cursor.execute(f"ALTER TABLE {table_name} DROP CONSTRAINT {constraint_name};")
            else:
                logging.warning(f"No foreign key constraint found for '{column_name}' on '{table_name}'.")
        except pyodbc.Error as e:
            logging.error(f"Error deleting foreign key constraint! {e}")
    
        if self.auto_commit:
            self.commit()

    def big_insert(self, table, values):
        """
        Matches values from a dict to the columns of a table and then inserts them.
    
        Args:
            table (str): The name of the table.
            values (dict): A dictionary containing column-value pairs for the data to be inserted.
        """
        if isinstance(self.get_columns_of_table(table), list) and isinstance(values, dict):
            try:
                data_to_insert = {key: values[key] for key in self.get_columns_of_table(table) if key in values}
                self.insert_into_table(table, data_to_insert)
            except:
                logging.error(f"Error batch inserting into {table}!")    
        else:
            logging.error(f"Error with values in batch insert into {table}! (Not lists! 'table' type is {type(self.get_columns_of_table(table))} and 'values' type is {type(values)})")

    def rollback(self):
        """
        Rollback the current database transaction.
        """
        logging.debug("Rolling back cursor.")
        self.cursor.rollback()

    def commit(self):
        """
        Commit the current database transaction.
        """
        self.cursor.commit()
        logging.debug(f"Data commited.")

INT_ID = "INT IDENTITY(1,1)"
LONG_CHAR = "VARCHAR(300)"
MED_CHAR = "VARCHAR(255)"
SHORT_CHAR = "VARCHAR(100)"
DATE = "DATE"
BOOL = "BIT"
TIMESTAMP = "VARCHAR(25)"