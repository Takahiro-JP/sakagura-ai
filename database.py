import sqlite3
from contextlib import contextmanager

DB_PATH = "data/sakagura.db"

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_db():
    with get_db() as conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS products (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            name         TEXT NOT NULL,
            series       TEXT,
            seimaibuai   INTEGER,
            price        REAL,
            flavor_notes TEXT,
            target_age   TEXT
        );

        CREATE TABLE IF NOT EXISTS post_history (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER REFERENCES products(id),
            platform   TEXT NOT NULL,
            content    TEXT NOT NULL,
            target     TEXT,
            created_at TEXT DEFAULT (datetime('now', 'localtime'))
        );

        CREATE TABLE IF NOT EXISTS analyze_history (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            filename   TEXT,
            result     TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now', 'localtime'))
        );
        """)

def add_product(name, series, seimaibuai, price, flavor_notes, target_age="全世代"):
    with get_db() as conn:
        cur = conn.execute(
            """INSERT INTO products
               (name, series, seimaibuai, price, flavor_notes, target_age)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (name, series, seimaibuai, price, flavor_notes, target_age)
        )
        return cur.lastrowid

def get_all_products():
    with get_db() as conn:
        rows = conn.execute("SELECT * FROM products").fetchall()
        return [dict(r) for r in rows]

def search_products(keyword):
    with get_db() as conn:
        rows = conn.execute(
            "SELECT * FROM products WHERE name LIKE ? OR series LIKE ?",
            (f"%{keyword}%", f"%{keyword}%")
        ).fetchall()
        return [dict(r) for r in rows]

def save_post(product_id, platform, content, target):
    with get_db() as conn:
        cur = conn.execute(
            """INSERT INTO post_history (product_id, platform, content, target)
               VALUES (?, ?, ?, ?)""",
            (product_id, platform, content, target)
        )
        return cur.lastrowid

def get_post_history(product_id=None, platform=None):
    query = """
        SELECT ph.*, p.name as product_name
        FROM post_history ph
        JOIN products p ON ph.product_id = p.id
    """
    params = []
    conditions = []
    if product_id:
        conditions.append("ph.product_id = ?")
        params.append(product_id)
    if platform:
        conditions.append("ph.platform = ?")
        params.append(platform)
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    query += " ORDER BY ph.created_at DESC"
    with get_db() as conn:
        return [dict(r) for r in conn.execute(query, params).fetchall()]

def save_analyze(filename: str, result: str):
    with get_db() as conn:
        conn.execute(
            "INSERT INTO analyze_history (filename, result) VALUES (?, ?)",
            (filename, result)
        )

def get_analyze_history():
    with get_db() as conn:
        rows = conn.execute(
            "SELECT * FROM analyze_history ORDER BY created_at DESC"
        ).fetchall()
        return [dict(r) for r in rows]
