from database import CursorFromConnectionFromPool

class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        
    def __repr__(self): # allows to print the object
        return("<User {}>".format(self.email))
        
    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)', 
                           (self.email, self.first_name, self.last_name))
    
    @classmethod # it doesn't access the currently bound object
    def load_from_db_by_email(cls, email): # cls is the currently bound class
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,)) # this is a tuple
            user_data = cursor.fetchone() # returns the first row
            return cls(email=user_data[1], first_name=user_data[2], 
                       last_name=user_data[3], id=user_data[0]) # we are returning a new object the class User
    

# ==============================VIDEO 97=======================================
# 
#     # the postgres user is a super user
#     def save_to_db(self):
#         #with connection_pool.getconn() as connection: # commit and close not needed explicitly
#         connection = connection_pool.getconn()
#         with connection.cursor() as cursor: # this opens and closes the cursor automatically
#             cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)', 
#                            (self.email, self.first_name, self.last_name))
#         connection_pool.putconn(connection)
# 
# 
#     @classmethod # it doesn't access the currently bound object
#     def load_from_db_by_email(cls, email): # cls is the currently bound class
#         #another_user = cls('TomHanks@hotmail.com', 'Tom', 'Hanks', None)
#         connection = connection_pool.getconn()
#         with connection.cursor() as cursor:
#             cursor.execute('SELECT * FROM users WHERE email = %s', (email,)) # this is a tuple
#             user_data = cursor.fetchone() # returns the first row
#             return cls(email=user_data[1], first_name=user_data[2], 
#                        last_name=user_data[3], id=user_data[0]) # we are returning a new object the class User
#         connection_pool.putconn(connection)
# =============================================================================

# ================================VIDEO 101========================================
#
#     def save_to_db(self):
#         with ConnectionFromPool() as connection:
#             with connection.cursor() as cursor: # this opens and closes the cursor automatically
#                 cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)', 
#                                (self.email, self.first_name, self.last_name))
#     
#     @classmethod # it doesn't access the currently bound object
#     def load_from_db_by_email(cls, email): # cls is the currently bound class
#         #another_user = cls('TomHanks@hotmail.com', 'Tom', 'Hanks', None)
#         with ConnectionFromPool() as connection:
#             with connection.cursor() as cursor:
#                 cursor.execute('SELECT * FROM users WHERE email = %s', (email,)) # this is a tuple
#                 user_data = cursor.fetchone() # returns the first row
#                 return cls(email=user_data[1], first_name=user_data[2], 
#                            last_name=user_data[3], id=user_data[0]) # we are returning a new object the class User
#
# =============================================================================
