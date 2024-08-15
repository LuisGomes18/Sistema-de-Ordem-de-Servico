from os import urandom
from flask import Flask, render_template, request, redirect, url_for
from config import conectar_bando_de_dados
from extras import gerar_id_cliente


app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(32)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cliente')
def cliente():
    return render_template('cliente/index.html')


@app.route('/cliente/listar', methods=('GET', 'POST'))
def listar_clientes():
    conn = conectar_bando_de_dados()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('cliente/listar_clientes.html', clientes=clientes)


@app.route('/cliente/criar', methods=('GET', 'POST'))
def criar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        telefone = request.form['contacto'] 
        email = request.form['email'] 
        informacoes = request.form['informacoes']  

        id = gerar_id_cliente() 

        conn = conectar_bando_de_dados()
        cursor = conn.cursor() 
        cursor.execute(
            'INSERT INTO clientes (id, nome, endereco, telefone, email, informacoes) VALUES (%s, %s, %s, %s, %s, %s)',
            (id, nome, endereco, telefone, email, informacoes),
        ) 
        conn.commit()
        cursor.close()
        conn.close()  

        return redirect(url_for('index'))  

    return render_template('cliente/criar_cliente.html') 


@app.route('/cliente/<int:id>/editar', methods=('GET', 'POST'))
def editar_cliente(id):
    conn = conectar_bando_de_dados()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM clientes WHERE id = %s', (id,))
    cliente = cursor.fetchone()

    if request.method == 'POST':
        nome = request.form['nome'] 
        endereco = request.form['endereco']  
        telefone = request.form['contacto']  
        email = request.form['email'] 
        informacoes = request.form['informacoes'] 

        cursor.execute(
            'UPDATE clientes SET nome = %s, endereco= %s, telefone = %s, email = %s, informacoes = %s WHERE id = %s',
            (nome, endereco, telefone, email, informacoes, id),
        )
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

    cursor.close()
    conn.close()
    return render_template('cliente/editar_cliente.html', cliente=cliente)


@app.route('/cliente/<int:id>/visualizar', methods=('GET', 'POST'))
def visualizar_cliente(id):
    conn = conectar_bando_de_dados()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM clientes WHERE id = %s', (id,))
    cliente = cursor.fetchone()
    cursor.close()
    conn.close()

    return render_template('cliente/ver_cliente.html', cliente=cliente)

@app.route('/ordem/')
def ordem():
    return render_template('ordem/index.html')

@app.route('/ordem/listar', methods=('GET', 'POST'))
def listar_ordens():
    conn = conectar_bando_de_dados()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM ordem_servico')
    ordens = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('ordem/listar_ordens.html', ordens=ordens)

@app.route('/ordem/criar', methods=('GET', 'POST'))
def criar_ordem():
    return "0"

@app.route('/ordem/<int:id>/editar', methods=('GET', 'POST'))
def editar_ordem(id):
    return "0"

@app.route('/ordem/<int:id>/visualizar', methods=('GET', 'POST'))
def visualizar_ordem(id):
    return "0"

@app.route('/ordem/<int:id>/apagar', methods=('GET', 'POST'))
def apagar_ordem(id):
    conn = conectar_bando_de_dados()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('DELETE FROM ordem_servico WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('listar_ordens'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
