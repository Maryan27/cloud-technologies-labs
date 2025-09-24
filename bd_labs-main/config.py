import os
import sys

os.environ['LANG'] = 'en_US.UTF-8'

sys.dont_write_bytecode = True

class Config:
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'iotparol1')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'solar_station')
