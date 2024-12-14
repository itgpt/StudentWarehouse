import os
try:
    from dotenv import load_dotenv
except ImportError:
    print('没有找到dotenv模块,需要安装: pip install dotenv')
    exit()
    
load_dotenv()
api_key = os.getenv('API_KEY')
db_password = os.getenv('DB_PASSWORD')
