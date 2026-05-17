import sqlite3
from datetime import date

conn = sqlite3.connect('store')

print("Database has been created")

conn.execute("DROP TABLE IF EXISTS pet")

conn.execute("CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), checkups SMALLINT UNSIGNED, birth DATE, death DATE)")

print("Table created successfully")

conn.execute("INSERT INTO pet (name,owner,species,sex,checkups,birth,death)VALUES \
  ('Fluffy','Harold','cat','f',5,'2001-02-04','')")

conn.execute("INSERT INTO pet (name,owner,species,sex,checkups,birth,death)VALUES \
  ('Claws','Gwen','cat','m',2,'2000-03-17','')")

conn.commit()
print("Records created successfully")
print("Total number of rows created:", conn.total_changes, "\n")

def printAllPets(conn: sqlite3.Connection):
    cursor = conn.execute("SELECT name,owner,species,sex,checkups,birth,death from pet")

    for row in cursor:
      print("name = ", row[0])
      print("owner = ", row[1])
      print("species = ", row[2])
      print("sex = ", row[3])
      print("checkups = ", row[4])
      print("birth = ", row[5])
      print("death = ", row[6], "\n")

printAllPets(conn)

today = date.today()
owner = "Harold"
name = "Fluffy"

def setPetDeath(conn: sqlite3.Connection, today: date, owner: str, name: str):
    conn.execute(f"UPDATE pet SET death='{today.strftime('%Y-%m-%d')}' WHERE owner='{owner}' AND name='{name}';")

    conn.commit()
    print("Record(s) updated successfully")
    print("Total number of rows updated:", conn.total_changes, "\n")

setPetDeath(conn, today, owner, name)

printAllPets(conn)
