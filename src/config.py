import os

HOST = os.getenv('API_BASE_URL', default='0.0.0.0')
PORT = os.getenv('API_PORT', default='80')
DEBUG = bool(os.getenv('API_DEBUG', default='True'))
