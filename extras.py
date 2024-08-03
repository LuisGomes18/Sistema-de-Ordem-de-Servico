from random import randint
from config import conectar_bando_de_dados


def gerar_id_cliente():
    """
    Generates a unique client ID by repeatedly generating random numbers 
    until a number is found that is not already in use.

    Returns:
        int: A unique client ID.
    """

    # Establish a connection to the MySQL database
    conn = conectar_bando_de_dados()

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Loop until a unique ID is found
    while True:

        # Generate a random number between 1000 and 9999
        id = randint(1000, 9999)

        # Construct a SELECT query to check if the generated ID is already in use
        query = 'SELECT * FROM clientes WHERE id = %s'

        # Execute the query with the generated ID as a parameter
        cursor.execute(query, (id,))

        # Fetch the result of the query
        user_id = cursor.fetchone()

        # If the generated ID is not already in use, exit the loop
        if not user_id:
            break

    # Close the cursor to free up database resources
    cursor.close()

    # Close the connection to the database
    conn.close()

    # Return the unique client ID
    return id
