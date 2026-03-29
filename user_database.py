import sqlite3

def get_user_by_id(user_id):
    """Fetch user from database - VULNERABLE to SQL injection"""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Direct string concatenation - SQL injection vulnerability
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    return result
