import sqlite3
import os

print("=" * 65)
print("  DecodeLabs Project 3 — The Data Warehouse")
print("  Operator: Selorm Tetteh-Abotsi")
print("  Infrastructure: AWS RDS MySQL (simulated locally)")
print("=" * 65)
print()

# Connect to local database (simulates RDS MySQL)
conn = sqlite3.connect("interndb.db")
cursor = conn.cursor()

print("[ OK ] Connected to database successfully.")
print()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Interns (
        InternID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName VARCHAR(50) NOT NULL,
        LastName  VARCHAR(50) NOT NULL,
        Email     VARCHAR(100) UNIQUE NOT NULL
    )
""")
print("[ OK ] Table 'Interns' created with PRIMARY KEY, UNIQUE, NOT NULL constraints.")
print()

# Insert records
records = [
    ('Selorm',  'Tetteh-Abotsi', 'selorm@decodelabs.com'),
    ('Jane',    'Smith',         'jsmith@decodelabs.com'),
    ('Kofi',    'Mensah',        'kmensah@decodelabs.com'),
    ('Ama',     'Owusu',         'aowusu@decodelabs.com'),
]

cursor.executemany(
    "INSERT OR IGNORE INTO Interns (FirstName, LastName, Email) VALUES (?, ?, ?)",
    records
)
conn.commit()
print(f"[ OK ] Inserted {cursor.rowcount} record(s) into Interns table.")
print()

# Verify persistence
print("Executing: SELECT * FROM Interns;")
print()
cursor.execute("SELECT * FROM Interns")
rows = cursor.fetchall()

print(f"{'InternID':<12} {'FirstName':<15} {'LastName':<20} {'Email'}")
print("-" * 65)
for row in rows:
    print(f"{row[0]:<12} {row[1]:<15} {row[2]:<20} {row[3]}")

print()
print("[ OK ] Data persisted successfully. Warehouse operational.")

cursor.close()
conn.close()