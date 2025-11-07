import os
import sys

os.environ['LANG'] = 'en_US.UTF-8'
sys.dont_write_bytecode = True


class Config:
    MYSQL_HOST = os.environ.get("MYSQL_HOST", "solar-db.cx2m2sw06cja.eu-central-1.rds.amazonaws.com")
    MYSQL_USER = os.environ.get("MYSQL_USER", "maryan_l")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "Iotir!34")
    MYSQL_DB = os.environ.get("MYSQL_DB", "solar")
    MYSQL_PORT = 3306

