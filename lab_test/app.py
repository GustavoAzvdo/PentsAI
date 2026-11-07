# app.py - Laboratório de Teste de Vulnerabilidade (SQL Injection)
# Cenário de demonstração para validação do agente de segurança ofensiva (PentsAI).

import sqlite3

def init_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'Sup3rS3cr3tP@ss!')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('operador', 'lab2026')")
    conn.commit()
    return conn

def login_vulneravel(conn, username, password):
    """
    VULNERÁVEL: Concatenação direta de strings na consulta SQL (CWE-89 / MITRE T1190).
    Permite bypass de autenticação com payload: ' OR 1=1 --
    """
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"[*] Query executada: {query}")
    cursor.execute(query)
    user = cursor.fetchone()
    return user

def login_corrigido(conn, username, password):
    """
    CORRIGIDO: Uso de consulta parametrizada (Prepared Statement).
    Neutraliza qualquer tentativa de SQL Injection tratando a entrada como dado literal.
    """
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    return user

if __name__ == '__main__':
    conn = init_db()
    print("=== Laboratório PentsAI / Validação de SQLi ===")
    
    # Teste 1: Exploração no código vulnerável
    payload = "' OR 1=1 --"
    print(f"\n[1] Tentando bypass no endpoint vulnerável com payload: {payload}")
    resultado = login_vulneravel(conn, payload, "qualquer_senha")
    if resultado:
        print(f"[!] SUCESSO NO BYPASS! Autenticado como: {resultado[1]}")
    
    # Teste 2: Validação da mitigação no código seguro
    print(f"\n[2] Testando o mesmo payload no endpoint corrigido...")
    resultado_seguro = login_corrigido(conn, payload, "qualquer_senha")
    if resultado_seguro:
        print("[!] Falha de segurança: o payload ainda passou!")
    else:
        print("[✓] MITIGAÇÃO EFETIVA: SQL Injection bloqueado com sucesso!")
