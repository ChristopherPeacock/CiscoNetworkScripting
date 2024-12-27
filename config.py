import os
from dotenv import load_dotenv

CSR = {
    'device_type': 'cisco_ios',
    'ip': os.getenv('IP'),
    'username': os.getenv('USERNAME'),
    'password': os.getenv('PASSWORD'),
    'port': 22,
}