# imports
import mariadb
import yaml
import sys
import os

# color codes for console
RED = '\033[31m'  # red
GREEN = '\033[32m'  # green
ORANGE = '\033[33m'  # orange
BLUE = '\033[34m'  # blue
PURPLE = '\033[35m'  # purple


# initializing global variables


# TODO: Local DNS Server with domain dowis.de to connect to web based interface


def error(ex):
    """function for printing failure report and safely ending program"""
    print(RED + "Error occurred while running program:")
    print(f"{ORANGE}{ex}")
    print(PURPLE + "Exiting now...")
    sys.exit()


def databaseConnection():
    """function to connect to MariaDB / MySQL Database"""
    try:
        # loading config file and storing values in variables
        with open("databaseconfig.yml", 'r') as configfile:
            cfg = yaml.safe_load(configfile)
            print("Connecting to database with following parameters:")
            print(f"Host: {cfg['db_host']}")
            print(f"User: {cfg['db_user']}")
            print(f"Password: {cfg['db_password']}")
            print(f"Database: {cfg['db_database']}")
            print(f"Port: {cfg['db_port']}")

            db_host = cfg["db_host"]
            db_port = cfg["db_port"]
            db_user = cfg["db_user"]
            db_password = cfg["db_password"]
            db_database = cfg["db_database"]
    except Exception as ex:
        error(ex)

    # connecting to database with data from config
    try:
        connection = mariadb.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database,
            port=db_port
        )
        cursor = connection.cursor()
        print(GREEN + "Conected to Database Successfully")
        return cursor, connection
    except mariadb.Error as ex:
        error(ex)




def basicDataFunction():
    pass


def main():
    """main program loop"""

    cursor, connection = databaseConnection()
    print(cursor)
    # start graphical user interface
    os.system("gui.py")


if __name__ == "__main__":
    main()
