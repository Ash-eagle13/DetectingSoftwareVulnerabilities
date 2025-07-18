import sqlite3
#hard-coded creditials (insecure)
username = "admin"
password = "admin123"
#Simulate login check
if username == "admin" and password == "admin123" :
    print ("Login successful")
    conn = sqlite3.connect ('example.db')
    print("Connected to database.")
else:
    print ("Login failed")