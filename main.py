import mariadb
import yaml
import sys


# TODO: Local DNS Server with domain dowis.de to connect to web based interface

def start():
    pass


def error(ex):
    print("Error reading config file for database:")
    print(ex)
    print("Exiting now...")
    sys.exit()


def databaseConnection():
    try:
        # loading config file and storing values in variables
        with open("databaseconfig.yml", 'r') as configfile:
            cfg = yaml.safe_load(configfile)
            db_host = cfg["db_host"]
            db_port = cfg["db_port"]
            db_user = cfg["db_user"]
            db_password = cfg["db_password"]
            db_database = cfg["db_database"]
    except Exception as ex:
        error(ex)

    try:
        connection = mariadb.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_database
        )

    except mariadb.Error as ex:
        error(ex)
    cursor = connection.cursor()

if __name__ == "__main__":
    start()
