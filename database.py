from psycopg2 import pool

#def connect():
#    return psycopg2.connect(user='postgres', password='foxi', database='learning', 
#                              host='localhost')
    


# in our case due to the with statement it is not developed when we write this:
# 'with connection_pool.getconn() as connection:', python was understanding this:
# 'connection = connection_pool.getconn(). And that is why it was exhausted too
# early. So or we put like like this: 'connection = connection_pool.getconn()'
# ... and then put back the conneciton 'connection_pool.putconn(connection' OR
# We implement the with statement for the connection. Let's implement it :D

#connection_pool = pool.SimpleConnectionPool(minconn=1, maxconn=1, 
#                                            user='postgres', 
#                                            password='foxi', 
#                                            database='learning', 
#                                            host='localhost')

class Database: # this lets us put connection_pool as global, and even control when to inicializate it
    __connection_pool = None # this makes the connection pool private
    
    # the connection pool belongs to the class, not to an object of the class
    # so that all objects we create of type Database will have the same connection pool
    @staticmethod # it is a clas method, even we car remove the cls and leave the () empty
    def initialise(minconn=1, maxconn=10, **kwargs): # not executed automatically
        Database.__connection_pool = pool.SimpleConnectionPool(minconn, 
                                                               maxconn, 
                                                               **kwargs)
        
    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()
    
    @classmethod
    def return_connection(cls, connection):
        return cls.__connection_pool.putconn(connection)
    
    @classmethod
    def close_all_connections(cls):
        cls.__connection_pool.closeall()


# =============================================================================
# class ConnectionFromPool: # this class represents one conexion from the global pool
#     def __init__(self):
#         self.connection = None # what I am going to keep track of each of the objects is the connection that it represents
# 
#     def __enter__(self): # ConnectionPool() calls __enter method at the start of the with statement, and afterwads the __init__
#         # self.connection = Database.connection_pool.getconn() # gets a connection from the pool
#         self.connection = Database.getconnection()
#         return self.connection # this object does have a cursor
#     
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.connection.commit()
#         # return self.connection_pool.putconn() # liberates the connection, doesn't return it
#         # Database.connection_pool.putconn(self.connection) # returns the connection to the pool :D
#         Database.return_connection(self.connection)
# =============================================================================
        
class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cusor = None

    def __enter__(self): # we get a cursor directly from the pool
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor
    
    # if an error happens during inserting, then we get the type, the value 
    # store and explanation message of where the error happen
    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None: # e.g. TypeError, AttributeError, ValueError
            self.connection.rollback() # when is an error, we delete all the data we put in the connection
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)