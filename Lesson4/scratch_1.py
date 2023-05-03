import sqlite3

try:
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    sql = """
        SELECT * FROM users;
    """
    cur.execute(sql)
    print(cur.fetchall())


    name = 'Jack'
    language = 'Python'

    sql_add_item = f"""
        INSERT INTO users
        VALUES ('{name}', '{language}', 'Pro', 30);
    """

    cur.execute(sql_add_item)
    conn.commit()

    cur.execute(sql)
    print(cur.fetchall())



finally:
    conn.close()
