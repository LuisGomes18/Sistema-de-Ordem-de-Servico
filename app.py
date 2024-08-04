from os import urandom
from flask import Flask, render_template, request, redirect, url_for
from config import conectar_bando_de_dados
from extras import gerar_id_cliente


app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(32)


@app.route('/')
def index():
    """
    This function is a route decorator that specifies the URL path for the
    root URL ('/') of our Flask application. When a user visits the root URL,
    this function is called to generate the HTML content for the page.

    This function has no parameters and does not accept any arguments.

    The function uses the 'render_template()' function, which is a built-in
    function in Flask. This function takes a template file name as an argument
    and renders the HTML content for that template file.

    The argument passed to 'render_template()' is the name of the template file
    that we want to use. In this case, we want to use the 'index.html' template
    file. The 'index.html' file is located in the 'templates' directory of our
    Flask application.

    The 'render_template()' function returns the rendered HTML content for the
    'index.html' template file. This content is then returned as the response to
    the user's request.

    So, when a user visits the root URL ('/') of our Flask application, they will
    see the rendered HTML content of the 'index.html' template file.

    Note: Template files are HTML files that contain placeholders for dynamic
    content. When we render a template file, we pass in data that can be used
    to populate the placeholders in the template file.

    In this case, we don't pass any data to the 'index.html' template file, so
    there are no placeholders to populate.

    The function does not contain any conditional statements or loops, so it will
    always execute the same way.

    The function does not return any values or raise any exceptions.

    The function does not perform any side effects, so it is considered a pure
    function.
    """
    # Call the 'render_template()' function to generate the HTML content for the
    # 'index.html' template file.
    # This function returns the rendered HTML content for the 'index.html'
    # template file.
    # The rendered HTML content is then returned as the response to the user's
    # request.
    return render_template('index.html')


@app.route('/cliente')
def cliente():
    """
    This function is a route decorator that specifies the URL path for the
    '/cliente' URL of our Flask application. When a user visits this URL,
    this function is called to generate the HTML content for the page.

    The function calls the 'render_template()' function, which is a built-in
    function in Flask that takes a template file name as an argument and renders
    the HTML content for that template file.

    The argument passed to 'render_template()' is the name of the template file
    that we want to use. In this case, we want to use the 'index.html' template
    file. The 'index.html' file is located in the 'templates/cliente' directory of
    our Flask application.

    The 'render_template()' function returns the rendered HTML content for the
    'index.html' template file. This content is then returned as the response to
    the user's request.

    So, when a user visits the '/cliente' URL of our Flask application, they will
    see the rendered HTML content of the 'index.html' template file located in the
    'templates/cliente' directory.

    Note: Template files are HTML files that contain placeholders for dynamic
    content. When we render a template file, we pass in data that can be used
    to populate the placeholders in the template file.

    In this case, we don't pass any data to the 'index.html' template file, so
    there are no placeholders to populate.
    """
    # Call the 'render_template()' function to generate the HTML content for the
    # 'index.html' template file located in the 'templates/cliente' directory.
    return render_template('cliente/index.html')


@app.route('/cliente/listar', methods=('GET', 'POST'))
def listar_clientes():
    '''
    This function is a route decorator that specifies the URL path for the
    '/cliente/listar' URL of our Flask application. When a user visits this URL,
    this function is called to generate the HTML content for the page.

    The function establishes a connection to the MySQL database using the
    'conectar_bando_de_dados()' function. This function is defined in the
    'banco_de_dados.py' file.

    The function then creates a cursor object to execute SQL queries using the
    'cursor()' method of the database connection object. The 'dictionary=True'
    parameter is set to True, which means that the result of the query will be
    returned as a list of dictionaries, where each dictionary represents a row
    in the result set.

    The function executes a SELECT query using the 'execute()' method of the
    cursor object. The query selects all records from the 'clientes' table.

    The function fetches all rows returned by the query using the 'fetchall()'
    method of the cursor object. The result is a list of dictionaries, where each
    dictionary represents a row in the result set.

    Once the query is executed and the result is fetched, the cursor and database
    connection objects are closed to free up resources.

    Finally, the function calls the 'render_template()' function to generate the
    HTML content for the 'listar_clientes.html' template file. The 'clientes'
    parameter is passed to the template file, which can be used to populate
    placeholders in the template file with the data from the 'clientes' variable.

    The 'render_template()' function returns the rendered HTML content for the
    'listar_clientes.html' template file. This content is then returned as the
    response to the user's request.

    So, when a user visits the '/cliente/listar' URL of our Flask application,
    they will see the rendered HTML content of the 'listar_clientes.html'
    template file, populated with data from the 'clientes' variable.

    Note: Template files are HTML files that contain placeholders for dynamic
    content. When we render a template file, we pass in data that can be used
    to populate the placeholders in the template file.
    '''

    # Establish a connection to the MySQL database
    conn = conectar_bando_de_dados()

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor(dictionary=True)

    # Execute a SELECT query to retrieve all records from the 'clientes' table
    cursor.execute('SELECT * FROM clientes')

    # Fetch all rows returned by the query as a list of dictionaries
    clientes = cursor.fetchall()

    # Close the cursor to free up database resources
    cursor.close()

    # Close the connection to the database
    conn.close()

    # Render the 'listar_clientes.html' template and pass the list of clientes as
    # a parameter. The 'render_template()' function will search for this template
    # file in the 'templates' directory of the Flask application package.
    return render_template('cliente/listar_clientes.html', clientes=clientes)


@app.route('/cliente/criar', methods=('GET', 'POST'))
def criar_cliente():
    '''
    This function handles the '/cliente/criar' URL endpoint. It is responsible for
    creating a new client in the database.

    If the request method is POST, it means that the user has submitted a form with
    client data. The function retrieves the form data, generates a unique ID for the
    new client, connects to the MySQL database, creates a cursor object to execute
    SQL queries, executes an INSERT query to add the new client to the 'clientes'
    table, commits the changes to the database, and closes the cursor and database
    connection. Finally, it redirects the user to the home page.

    If the request method is not POST, it renders the 'criar_cliente.html' template
    file, which is used to display a form for creating a new client.
    '''

    # Check if the request method is POST
    if request.method == 'POST':

        # Get the form data
        nome = request.form['nome']  # This field is for the client's name
        endereco = request.form['endereco']  # This field is for the client's address
        telefone = request.form['contacto']  # This field is for the client's phone number
        email = request.form['email']  # This field is for the client's email address
        informacoes = request.form['informacoes']  # This field is for additional information about the client

        # Generate a unique ID for the new client
        id = gerar_id_cliente()  # This function generates a unique ID for the client

        # Connect to the MySQL database
        conn = (
            conectar_bando_de_dados()
        )  # This function establishes a connection to the MySQL database

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()  # This object is used to execute SQL queries on the database

        # Execute an INSERT query to add the new client to the 'clientes' table
        cursor.execute(
            'INSERT INTO clientes (id, nome, endereco, telefone, email, informacoes) VALUES (%s, %s, %s, %s, %s, %s)',
            (id, nome, endereco, telefone, email, informacoes),
        )  # This query inserts the new client's data into the 'clientes' table

        # Commit the changes to the database
        conn.commit()  # This commits the changes made to the database

        # Close the cursor to free up database resources
        cursor.close()  # This closes the cursor object, freeing up database resources

        # Close the connection to the database
        conn.close()  # This closes the connection to the database

        # Redirect the user to the home page
        return redirect(url_for('index'))  # This redirects the user to the home page of the application

    # If the request method is not POST, render the 'criar_cliente.html' template
    return render_template('cliente/criar_cliente.html')  # This renders the 'criar_cliente.html' template file


@app.route('/cliente/<int:id>/editar', methods=('GET', 'POST'))
def editar_cliente(id):
    '''
    This function handles the '/cliente/<int:id>/editar' URL endpoint.
    It is responsible for editing a client in the database.

    If the request method is POST, it means that the user has submitted a form
    with client data. The function retrieves the form data, executes an UPDATE
    query to update the client with the specified ID, commits the changes to
    the database, and redirects the user to the home page.

    If the request method is not POST, it renders the 'editar_cliente.html'
    template file, which is used to display a form for editing a client.
    '''

    # Connect to the MySQL database
    conn = conectar_bando_de_dados()

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor(dictionary=True)

    # Execute a SELECT query to retrieve the client with the specified ID
    cursor.execute('SELECT * FROM clientes WHERE id = %s', (id,))

    # Fetch the first (and only) row from the result set
    cliente = cursor.fetchone()

    # Check if the request method is POST
    if request.method == 'POST':
        # Get the form data
        nome = request.form['nome']  # Get the value of the 'nome' field from the form
        endereco = request.form['endereco']  # Get the value of the 'endereco' field from the form
        telefone = request.form['contacto']  # Get the value of the 'contacto' field from the form
        email = request.form['email']  # Get the value of the 'email' field from the form
        informacoes = request.form['informacoes']  # Get the value of the 'informacoes' field from the form

        # Execute an UPDATE query to update the client with the specified ID
        cursor.execute(
            'UPDATE clientes SET nome = %s, endereco= %s, telefone = %s, email = %s, informacoes = %s WHERE id = %s',
            (nome, endereco, telefone, email, informacoes, id),
        )

        # Commit the changes to the database
        conn.commit()

        # Close the cursor to free up database resources
        cursor.close()

        # Close the connection to the database
        conn.close()

        # Redirect the user to the home page
        return redirect(url_for('index'))

    # If the request method is not POST, render the 'editar_cliente.html' template
    # with the client data passed as a parameter
    cursor.close()
    conn.close()
    return render_template('cliente/editar_cliente.html', cliente=cliente)


@app.route('/cliente/<int:id>/visualizar', methods=('GET', 'POST'))
def visualizar_cliente(id):
    '''
    This function handles the '/cliente/<int:id>/visualizar' URL endpoint.
    It is responsible for displaying the details of a client in the database.

    Parameters:
        id (int): The ID of the client to be displayed.

    Returns:
        The rendered 'ver_cliente.html' template with the client data passed as a parameter.
        The client data is passed as a parameter named 'cliente' and can be accessed in the template using the 'cliente' variable.

    Description:
        This function establishes a connection to the MySQL database using the 'conectar_bando_de_dados()' function.
        It then creates a cursor object to execute SQL queries using the 'cursor()' method of the database connection object.
        The function executes a SELECT query using the 'execute()' method of the cursor object to retrieve the client with the specified ID.
        The result is fetched using the 'fetchone()' method of the cursor object, and stored in the 'cliente' variable.
        The cursor and database connection objects are closed to free up resources.
        Finally, the function calls the 'render_template()' function to generate the HTML content for the 'ver_cliente.html' template file.
        The 'cliente' parameter is passed to the template file, which can be used to populate placeholders in the template file with the data from the 'cliente' variable.
        The 'render_template()' function returns the rendered HTML content for the 'ver_cliente.html' template file.
        This content is then returned as the response to the user's request.
    '''
    # Connect to the MySQL database
    conn = conectar_bando_de_dados()

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor(dictionary=True)

    # Execute a SELECT query to retrieve the client with the specified ID
    cursor.execute('SELECT * FROM clientes WHERE id = %s', (id,))

    # Fetch the first (and only) row from the result set
    cliente = cursor.fetchone()

    # Close the cursor to free up database resources
    cursor.close()

    # Close the connection to the database
    conn.close()

    # Render the 'ver_cliente.html' template with the client data passed as a parameter
    # The client data is passed as a parameter named 'cliente'
    # This allows us to access the client data in the template using the 'cliente' variable
    return render_template('cliente/ver_cliente.html', cliente=cliente)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
