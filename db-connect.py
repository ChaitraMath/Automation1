import sqlite3

def main():
    db = sqlite3.connect(":memory:")
    cur = db.cursor

    db.execute("SELECT sqlite_version()")
    version = db.fetchone()[0]
    print(f"SQLite version {version}")

    cur.close()
    db.close()

if __name__ == "__main__":
    main()