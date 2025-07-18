import sqlite3
import getpass
#secure input method
username = input ("Enter username: ")
password = getpass.getpass ("Enter password: ")
if username == "admin" and password == "admin123":
    print ("Login successful")
    conn = sqlite3.connect('example.db')
    print ("connected to database.")
else:
    print ("Login failed")