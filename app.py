from user import User
from database import Database

# my_user = User('jose@schoolofcode.me', 'Jose', 'Salvatierra', None)
# my_user = User('pepecontrapepe@gmail.com', 'Jose Ramon', 'Gene Garrigos', None)

# print(my_user)

#my_user.save_to_db()

# the classmethod is called directly from the class
# my_user = User.load_from_db_by_email('jose@schoolofcode.me')
# print(my_user)

def introduce_data():
    email = input('Introduce email: ')
    first_name = input('Introduce first name: ')
    last_name = input('Introduce last name: ')

    new_user = User(email, first_name, last_name, None)
    new_user.save_to_db()
    print('User introduced. Check the DataBase')
    
# introduce_data()
    
Database.initialise(user='postgres', password='foxi',
                    database='learning', host='localhost')
    
my_user = User('AliciaHarris@baila.mad', 'Alicia', 'Harris', None)

my_user.save_to_db()

my_user = User.load_from_db_by_email('AliciaHarris@baila.mad')

print(my_user)