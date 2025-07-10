import sqlite3
import os

DATABASE_DIR = 'data'
DATABASE_FILE = os.path.join(DATABASE_DIR, 'hit_count.db')

def init_db():
    """Inicializa la base de datos si no existe"""
    # Crear directorio si no existe
    os.makedirs(DATABASE_DIR, exist_ok=True)
    
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hits (
            id INTEGER PRIMARY KEY,
            count INTEGER DEFAULT 0
        )
    ''')
    
    # Insertar registro inicial si no existe
    cursor.execute('SELECT COUNT(*) FROM hits')
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO hits (count) VALUES (0)')
    
    conn.commit()
    conn.close()

def get_hit_count():
    """Incrementa y retorna el contador de visitas desde SQLite"""
    init_db()
    
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Incrementar contador atómicamente
    cursor.execute('UPDATE hits SET count = count + 1 WHERE id = 1')
    cursor.execute('SELECT count FROM hits WHERE id = 1')
    count = cursor.fetchone()[0]
    
    conn.commit()
    conn.close()
    
    return count
