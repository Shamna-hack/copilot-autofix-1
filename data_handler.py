import pickle
import os

def load_user_data(filename):
    """Load user data from file - VULNERABLE to deserialization attacks"""
    
    # Unsafe pickle deserialization
    with open(filename, 'rb') as f:
        user_data = pickle.load(f)  # Arbitrary code execution risk
    
    return user_data

def process_json_input(user_input):
    """Process user input - VULNERABLE to code injection"""
    
    # Using eval on user input is extremely dangerous
    result = eval(user_input)  # Can execute arbitrary code
    
    return result
