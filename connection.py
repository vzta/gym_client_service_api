import yaml
from pathlib import Path
import psycopg2

current_dir = Path.cwd()
yaml_dir = current_dir/"configs.yaml"
with open (yaml_dir) as config_file:
    config = yaml.safe_load(config_file)

db_host = config["db"]["host"]
db_name = config["db"]["database"]
db_user = config["db"]["user"]
db_password = config["db"]["password"]

def connection():
    '''
    connection Creation to the DB
    Returns the connection to the DB
    Args:
        db_host (str) 
        db_name (str)
        db_user (str)
        db_password (str) 
    '''
    conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password
)   
    return conn 
