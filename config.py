from os import getenv
from dotenv import load_dotenv
import mysql.connector


def conectar_bando_de_dados():
    """
    Function to establish a connection to the database.
    
    This function loads the environment variables from the .env file,
    and uses them to create a connection to a MySQL database. 
    
    Returns:
        connection (mysql.connector.connection.MySQLConnection): The connection object 
        representing the connection to the database.
    """

    # Load the environment variables from the .env file
    load_dotenv()

    # Create a connection to the MySQL database using the environment variables
    connection = mysql.connector.connect(
        host=getenv("DB_HOST"),  # The hostname of the database server
        user=getenv("DB_USERNAME"),  # The username to use for authentication
        password=getenv("DB_PASSWORD"),  # The password to use for authentication
        database=getenv("DB_DATABASE"),  # The name of the database to connect to
    )

    # Return the connection object
    return connection
