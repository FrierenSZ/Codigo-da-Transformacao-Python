import sqlite3
from sqlite3 import Error


DATABASE_FILE = "modulo_11/tarefas.db"

def criar_conexao(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conn

def criar_tabela(conn):
    sql_create_tasks_table = """ CREATE TABLE IF NOT EXISTS tarefas (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        descricao TEXT NOT NULL,
                                        concluida BOOLEAN NOT NULL CHECK (concluida IN (0, 1)) DEFAULT 0
                                    ); """
    try:
        c = conn.cursor()
        c.execute(sql_create_tasks_table)
    except Error as e:
        print(f"Erro ao criar a tabela: {e}")

def adicionar_tarefa(conn, descricao):
    sql = ''' INSERT INTO tarefas(descricao, concluida)
              VALUES(?,?) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, (descricao, 0)) 
        conn.commit()
        print(f" Tarefa '{descricao}' adicionada com sucesso! (ID: {cur.lastrowid})")
    except Error as e:
        print(f"Erro ao adicionar tarefa: {e}")

def visualizar_tarefas(conn):
    sql = "SELECT id, descricao, concluida FROM tarefas ORDER BY id"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        if not rows:
            print("\nNenhuma tarefa na lista.")
            return

        print("\n Lista de Tarefas:")
        print("-" * 35)
        for row in rows:
            status = "[CONCLUÍDA]" if row[2] == 1 else "[PENDENTE]"
            print(f"ID: {row[0]:<3} | {status:<12} | Tarefa: {row[1]}")
        print("-" * 35)

    except Error as e:
        print(f"Erro ao visualizar tarefas: {e}")

def excluir_tarefa(conn, task_id):
    sql = 'DELETE FROM tarefas WHERE id=?'
    try:
        cur = conn.cursor()
        cur.execute(sql, (task_id,))
        conn.commit()
        if cur.rowcount > 0:
            print(f" Tarefa com ID {task_id} excluída com sucesso.")
        else:
            print(f" Não foi encontrada nenhuma tarefa com o ID {task_id}.")
    except Error as e:
        print(f"Erro ao excluir tarefa: {e}")


def menu_principal():
    print("\n" + "="*30)
    print("  GERENCIADOR DE TAREFAS")
    print("="*30)
    print("1. Adicionar Tarefa")
    print("2. Visualizar Tarefas")
    print("3. Excluir Tarefa")
    print("4. Sair")
    print("="*30)

def main():
    conn = criar_conexao(DATABASE_FILE)

    if conn is not None:
        criar_tabela(conn)
        while True:
            menu_principal()
            escolha = input("Selecione uma opção: ")

            if escolha == '1':
                descricao = input("Digite a descrição da nova tarefa: ")
                if descricao:
                    adicionar_tarefa(conn, descricao.strip())
                else:
                    print("A descrição da tarefa não pode estar vazia.")

            elif escolha == '2':
                visualizar_tarefas(conn)

            elif escolha == '3':
                visualizar_tarefas(conn)
                try:
                    task_id = int(input("Digite o ID da tarefa que deseja excluir: "))
                    excluir_tarefa(conn, task_id)
                except ValueError:
                    print("ID inválido. Por favor, digite um número.")

            elif escolha == '4':
                print("Saindo do Gerenciador de Tarefas. Até logo!")
                break

            else:
                print("Opção inválida. Tente novamente.")

        conn.close() 
    else:
        print("Não foi possível estabelecer a conexão com o banco de dados.")

if __name__ == '__main__':
    main()