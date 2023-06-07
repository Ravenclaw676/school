import sqlite3 as sql

from getpass import getpass
from secrets import token_urlsafe

def hashing_algorithm(text: str, value) -> str:
    total = 0
    for letter in text:
        number = ord(letter)
        number = (number % value) * 10
        total += number

    hashed = total % value
    return hashed

BYTES = 8
MOD_VALUE = 5

file = sql.connect("sql/database.db")
cursor = file.cursor()

cursor.execute("""
CREATE TABLE users (
    userID INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    salt TEXT,
)""")

cursor.execute("""
CREATE TABLE quiz_scores (
    id INTEGER PRIMARY KEY,
    userID INTEGER,
    score INTEGER,
    FOREIGN KEY userID REFERENCES users.userID
)""")
               
cursor.execute("""
CREATE TABLE studentInfo(
    id INTEGER PRIMARY KEY,
    userID INTEGER,
    name TEXT,
    age INTEGER,
    gender TEXT
    FOREIGN KEY userID REFERENCECS users.userID
)""")
               
salt = token_urlsafe(BYTES)
username = input("please enter a username: ")
password = getpass() + salt
userID = hashing_algorithm(username + password, MOD_VALUE)

cursor.execute("""
INSERT INTO users\n
VALUES (?, ?, ?, ?)""", (userID ,username, hashing_algorithm(password, MOD_VALUE), salt))