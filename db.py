import psycopg2

"""
Sample contact response
    {
      "data": {
        "id": 1,
        "creator_id": 1,
        "owner_id": 1,
        "is_organization": true,
        "contact_id": null,
        "parent_organization_id": 2,
        "name": "Design Services Company",
        "first_name": null,
        "last_name": null,
        "customer_status": "none",
        "prospect_status": "none",
        "title": null,
        "description": null,
        "industry": "Design Services",
        "website": "http://www.designservice.com",
        "email": null,
        "phone": null,
        "mobile": null,
        "fax": "+44-208-1234567",
        "twitter": null,
        "facebook": null,
        "linkedin": null,
        "skype": null,
        "address": {
          "line1": "2726 Smith Street",
          "city": "Hyannis",
          "postal_code": "02601",
          "state": "MA",
          "country": "US"
        },
        "billing_address": null,
        "shipping_address": null,
        "tags": [
          "important"
        ],
        "custom_fields": {
          "known_via": "tom"
        },
        "created_at": "2014-08-27T16:32:56Z",
        "updated_at": "2014-08-27T16:32:56Z"
      }
"""

class DatabaseHandler():

    @classmethod
    def connect_to_db(cls):
        
        connection = psycopg2.connect(
                host="localhost",
                database="zendesk",
                user="postgres",
                password="Aphrodite666"
        )

        cursor = connection.cursor()

        return connection, cursor

    def create_tables(self):

        connection, cursor = self.connect_to_db()

        commands = (
            """
            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
            )
            """,
            """
            CREATE TABLE contacts (
                contact_id INTEGER PRIMARY KEY,
                FOREIGN KEY (user_id)
                name VARCHAR(255) NOT NULL,
            )
            """,
            """ 
            CREATE TABLE opportunities (
                opportunity_id INTEGER PRIMARY KEY,
                FOREIGN KEY (user_id)
                name VARCHAR(255) NOT NULL
            )
            """
        )
        
        for command in commands:
            cursor.execute(command)
        
        cursor.close()
        
        connection.commit()

    def save_contact_to_db(self, contact: dict):

        connection, cursor = self.connect_to_db()

        command = """INSERT INTO contacts(contact_name) VALUES(%s) RETURNING contact_id;"""

        # cursor.executemany(command, contact)
        cursor.execute(command, (contact['name'],))
        
        vendor_id = cursor.fetchone()[0]
        
        connection.commit()
        
        cursor.close()

    def save_opportunity_to_db(self, opportunity: dict):

        pass


if __name__ == '__main__':
    DatabaseHandler().create_tables()