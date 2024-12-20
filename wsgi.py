import sys
import os
from index import app  # Assuming your main bot script is index.py

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [b"Bot is running..."]  # Add actual response if needed
