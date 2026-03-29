# Configuration file - VULNERABLE with hardcoded secrets

API_KEY = "sk_live_51234567890abcdefghijk"
DATABASE_PASSWORD = "admin_password_123"
STRIPE_SECRET_KEY = "rk_live_test1234567890"

def connect_to_database():
    """Connect using hardcoded credentials"""
    host = "db.example.com"
    user = "admin"
    password = "SuperSecure@123"  # Hardcoded password
    
    connection = establish_db_connection(host, user, password)
    return connection
