import sys
import sqlite3
from pathlib import Path
from datetime import datetime


class Contacts:
    def __init__(self, db_path):
        self.db_path = db_path
        if not db_path.exists():
            print("Migrating db")
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()
            cursor.execute(
                """
                CREATE TABLE contacts(
                  id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL
                );
              """
            )
            connection.commit()
            cursor.execute("CREATE UNIQUE INDEX index_contacts_email ON contacts(email);")
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row

    def find_contact_with_email(self, email):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT * FROM contacts
            WHERE email = ?
            """,
            (email,),
        )
        return cursor.fetchone()


def insert_many_contacts(num_contacts):
    try:
        print(f"Inserting {num_contacts} contacts ...")
        # TODO - at the end of the call,
        # the database should contain `num_contacts` contacts,
        # from `email-1@domain.tod` to `email-{num_contacts}@domain.tld`,
        # in this order
        
        connection = sqlite3.connect("contacts.sqlite3")
        cursor = connection.cursor()
        

        cursor.execute("PRAGMA journal_mode = OFF;")
        cursor.execute("PRAGMA synchronous = 0;")
        cursor.execute("PRAGMA cache_size = 1000000;")
        cursor.execute("PRAGMA locking_mode = EXCLUSIVE;")
        cursor.execute("PRAGMA temp_store = MEMORY;")
    
        cursor.execute("DELETE FROM contacts")

        insert_query = "INSERT INTO contacts (name, email) VALUES (?, ?)"
        batch_size = 10000

        # Prepare the data and insert in batches
        for batch_start in range(0, num_contacts, batch_size):
            contacts = [(f"contact-{i}", f"email-{i}@domain.tld") 
                for i in range(batch_start + 1, min(batch_start + batch_size, num_contacts) + 1)]
            cursor.executemany(insert_query, contacts)
        

        connection.commit()
        
        cursor.execute("PRAGMA synchronous = FULL;")
        cursor.execute("PRAGMA journal_mode = DELETE;")
        cursor.execute("PRAGMA cache_size = 2000;")
        cursor.execute("PRAGMA locking_mode = NORMAL;")
        cursor.execute("PRAGMA temp_store = DEFAULT;")

        print("Done")

        cursor.execute("SELECT COUNT(*) FROM contacts")
        count = cursor.fetchone()[0]
        print(f"Number of contacts: {count}")
        connection.close()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        sys.exit("Not enough arguments")
    num_contacts = int(sys.argv[1])
    db_path = Path("contacts.sqlite3")

    contacts = Contacts(db_path)

    start = datetime.now()
    insert_many_contacts(num_contacts)
    end = datetime.now()
    elapsed = end - start
    print(f"insert_many_contacts took {elapsed.total_seconds() * 1000:.0f} ms")

    last_mail = f"email-{num_contacts}@domain.tld"
    print("Looking for email", last_mail)
    start = datetime.now()
    result = contacts.find_contact_with_email(f"email-{num_contacts}@domain.tld")
    end = datetime.now()
    elapsed = end - start
    print(f"find_contact_with_email took {elapsed.total_seconds() * 1000:.0f} ms")
    if not result:
        sys.exit(f"contact with email {last_mail} not found")


if __name__ == "__main__":
    main()
