'''


'''

import sqlite3

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect('modulo_11/clientes.db')

# Função para criar a tabela de clientes
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

# Operação para inserir um cliente
def inserir_cliente(nome, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', (nome, email))
    conn.commit()
    conn.close()

# Operação para consultar todos os clientes
def consultar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    conn.close()
    return clientes

# Operação para consultar um cliente por ID
def consultar_cliente_por_id(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes WHERE id = ?', (id,))
    cliente = cursor.fetchone()
    conn.close()
    return cliente

# Operação para atualizar um cliente
def atualizar_cliente(id, nome, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE clientes SET nome = ?, email = ? WHERE id = ?', (nome, email, id))
    conn.commit()
    conn.close()

# Operação para deletar um cliente
def deletar_cliente(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM clientes WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# Função principal para demonstrar as operações
if __name__ == '__main__':
    criar_tabela()

    # Inserir alguns clientes
    inserir_cliente('João Silva', 'joao@example.com')
    inserir_cliente('Maria Santos', 'maria@example.com')

    # Consultar todos os clientes
    print("Clientes:")
    for cliente in consultar_clientes():
        print(cliente)

    # Consultar um cliente específico
    cliente = consultar_cliente_por_id(1)
    print(f"\nCliente com ID 1: {cliente}")

    # Atualizar um cliente
    atualizar_cliente(1, 'João Silva Atualizado', 'joao.atualizado@example.com')

    # Consultar novamente
    cliente = consultar_cliente_por_id(1)
    print(f"\nCliente atualizado: {cliente}")

    # Deletar um cliente
    deletar_cliente(2)

    # Consultar todos novamente
    print("\nClientes após deletar:")
    for cliente in consultar_clientes():
        print(cliente)
