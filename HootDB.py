import sqlite3

conn = sqlite3.connect('HootData.db')
conn.execute("PRAGMA foreign_keys = 1")

c = conn.cursor()

T1 = """CREATE TABLE IF NOT EXISTS
tickets(id INTEGER PRIMARY KEY AUTOINCREMENT, issue TEXT)"""

T2 = """CREATE TABLE IF NOT EXISTS
comments(commentID INTEGER PRIMARY KEY, ticketID INTEGER, comment TEXT, 
FOREIGN KEY(ticketID) REFERENCES tickets(id))"""


c.execute(T1)
c.execute(T2)
conn.close()


def showAll():
    con = sqlite3.connect('HootData.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM tickets")
    items = cur.fetchall()

    for item in items:
        print("Ticket ID [", item[0], "]:", item[1])

    con.close()

def addTicket(issue):
    con = sqlite3.connect('HootData.db')
    cur = con.cursor()
    db = "INSERT INTO tickets (issue) VALUES (?)"
    cur.execute(db, (issue,))
    print("\"", issue, "\"")
    con.commit()
    con.close()

def addComment(id, comment):
    con = sqlite3.connect('HootData.db')
    cur = con.cursor()
    db = "INSERT INTO comments (comment, ticketID) VALUES (?, ?)"
    cur.execute(db, (comment, id))
    print("\"", comment, "\"")
    con.commit()
    con.close()

def viewTicket(num):
    con = sqlite3.connect('HootData.db')
    cur = con.cursor()
    cur.execute('SELECT issue FROM tickets WHERE id=?', num)
    print("Ticket ID [", num, "]:", cur.fetchone()[0])
    cur.execute('SELECT * FROM comments WHERE ticketID=?', num)
    items = cur.fetchall()
    count = 1
    for item in items:
        print("[", count, "]:", item[2])
        count += 1
    con.close()

def getLastId():
    con = sqlite3.connect('HootData.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM tickets')
    max_id = len(cur.fetchall())
    con.close()
    return max_id


