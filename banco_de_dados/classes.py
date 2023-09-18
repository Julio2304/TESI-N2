from pathlib import Path
import sqlite3

ROOT_DIR = Path(__file__).parent
DB_NAME = 'banco.db'
DB_FILE = ROOT_DIR / DB_NAME

TABLE_NAME = 'CLASSES'

def cria_conexao_banco():
    conexao = sqlite3.Connection(DB_FILE)
    cursor = conexao.cursor()
    sql = (
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            ' id_classe INTEGER PRIMARY KEY AUTOINCREMENT,'
            ' nome_classe TEXT UNIQUE NOT NULL,'
            ' constituicao_classe INTEGER DEFAULT 0,'
            ' forca_classe INTEGER DEFAULT 0,'
            ' inteligencia_classe INTEGER DEFAULT 0,'
            ' carisma_classe INTEGER DEFAULT 0,'
            ' agilidade_classe INTEGER DEFAULT 0'
        ')'
    )
    cursor.execute(sql)
    return conexao, cursor

def insere_valores(*args):
    conexao, cursor = cria_conexao_banco()
    sql = (
        f'INSERT INTO {TABLE_NAME} ( '
            ' nome_classe, constituicao_classe, forca_classe, inteligencia_classe, carisma_classe, agilidade_classe'
        ')'
        ' VALUES (?, ?, ?, ?, ?, ?)'
    )
    try:
        cursor.execute(sql, (args))
        conexao.commit()
        cursor.close()
        conexao.close()
    except Exception as e:
        print("Classe já existente na tabela, por favor insira outra. -> ", e, "-> ", args[0])
        cursor.close()
        conexao.close()
        
def mostra_todos():
    conexao, cursor = cria_conexao_banco()
    sql = F'SELECT * FROM {TABLE_NAME}'
    cursor.execute(sql)
    print(cursor.fetchall())
    cursor.close()
    conexao.close()
    
def seleciona_por_nome(nome):
    conexao, cursor = cria_conexao_banco()
    sql = f'SELECT * FROM {TABLE_NAME} WHERE nome_classe = ?'
    cursor.execute(sql, [nome])
    classe = cursor.fetchall()
    conexao.commit()
    cursor.close()
    conexao.close()
    return classe

def seleciona_por_id(id):
    conexao, cursor = cria_conexao_banco()
    sql = f'SELECT * FROM {TABLE_NAME} WHERE id_classe = ?'
    cursor.execute(sql, [id])
    classe = cursor.fetchall()
    conexao.commit()
    cursor.close()
    conexao.close()
    return classe
    
def limpa_todos():
    conexao, cursor = cria_conexao_banco()
    sql = F'DELETE FROM {TABLE_NAME}'
    cursor.execute(sql)
    conexao.commit()
    cursor.close()
    conexao.close()

# limpa_todos()
insere_valores('guerreiro', '0', '0', '546', '3', '5')
insere_valores('dasdsa', '0', '0', '546', '3', '5')
insere_valores('guerr2', '0', '0', '546', '3', '5')
insere_valores('aksdkasdk', '0', '0', '546', '3', '5')
insere_valores('kakkakakak', '0', '0', '546', '3', '5')
mostra_todos()
print('\nseparação aqui\n')
seleciona_por_nome('guerreiro')
seleciona_por_id('2')
    
    
