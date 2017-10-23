from database import connect

class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        
    def __repr__(self): # allows to print the object
        return("<User {}>".format(self.email))
        
    # the postgres user is a super user
    def save_to_db(self):
        with connect() as connection: # commit and close not needed explicitly
            with connection.cursor() as cursor: # this opens and closes the cursor automatically
                cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)', 
                               (self.email, self.first_name, self.last_name))
                
    @classmethod # it doesn't access the currently bound object
    def load_from_db_by_email(cls, email): # cls is the currently bound class
        #another_user = cls('TomHanks@hotmail.com', 'Tom', 'Hanks', None)
        with connect() as connection: # commit and close not needed explicitly
            with connection.cursor() as cursor: # this opens and closes the cursor automatically
                cursor.execute('SELECT * FROM users WHERE email = %s', (email,)) # this is a tuple
                user_data = cursor.fetchone() # returns the first row
                return cls(email=user_data[1], first_name=user_data[2], 
                           last_name=user_data[3], id=user_data[0]) # we are returning a new object the class User