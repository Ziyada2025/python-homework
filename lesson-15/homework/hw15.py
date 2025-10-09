import sqlite3 
connection=sqlite3.connect('Sample.db') 
cursor=connection.cursor() 
query=''' Create table Roster (Name VARCHAR (100), Species VARCHAR (100), Age INT)''' 
query2='''INSERT INTO Roster (Name, Species, Age) VALUES
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29); ''' 
t1=cursor.execute(query) 
t2=cursor.execute(query2) 


updatedquery=cursor.execute("Update Roster Set Name='Ezri Dax' Where Name='Jadzia Dax'")

cursor.execute('''
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
''') 
for row in cursor.fetchall():
    print(row)

