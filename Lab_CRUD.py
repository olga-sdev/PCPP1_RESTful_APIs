"""
Objectives

Learn how to:
use the requests module facilities;
build large software solutions using top-down tactics;
cooperate with a remote database using REST.

Scenario
Write a software solution managing a database that gathers data about vintage cars.
The criteria:


+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 1
*** Database is empty ***
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 2
Car ID (empty string to exit): 1
Car brand (empty string to exit): Porsche
Car model (empty string to exit): 911
Car production year (empty string to exit): 1963
Is this car convertible? [y/n] (empty string to exit): n
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 2
Car ID (empty string to exit): 2
Car brand (empty string to exit): Ford
Car model (empty string to exit): Mustang
Car production year (empty string to exit): 1972
Is this car convertible? [y/n] (empty string to exit): y
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 1
id        | brand          | model     | production_year     | convertible    |
1         | Porsche        | 911       | 1963                | False          |
2         | Ford           | Mustang   | 1972                | True           |

+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4):  4
Car ID (empty string to exit): 2
Car brand (empty string to exit): Ford
Car model (empty string to exit): Mustang
Car production year (empty string to exit): 1973
Is this car convertible? [y/n] (empty string to exit): n
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 3
Car ID (empty string to exit): 1
Success!
Car ID (empty string to exit):
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 0
Bye!
"""
import requests
import json


def check_server(cid=None):
    """
    returns True or False;
    when invoked without arguments simply checks if server responds;
    invoked with car ID checks if the ID is present in the database;
    """
    if requests.get('http://localhost:3000/'):
        return True
    else:
        return False


def print_menu():
    """prints user menu - nothing else happens here;"""
    print_header()
    global choice
    print("M E N U\n"
          "=======\n"
          "1. List cars\n"
          "2. Add new car\n"
          "3. Delete car\n"
          "4. Update car\n"
          "0. Exit\n")
    choice = input("Enter your choice (0..4): ")


def read_user_choice():
    """
    reads user choice and checks if it's valid;
    returns '0', '1', '2', '3' or '4'
    """
    if choice == '0':
        return '0'
    elif choice == '1':
        return '1'
    elif choice == '2':
        return '2'
    elif choice == '3':
        return '3'
    elif choice == '4':
        return '4'


def print_header():
    """prints elegant cars table header;"""
    print(
        "+-----------------------------------+\n"
        "|       Vintage Cars Database       |\n"
        "+-----------------------------------+\n"
    )

def list_cars():
    """
    gets all cars' data from server and prints it;
    if the database is empty prints diagnostic message instead;
    """
    get_reply = requests.get('http://localhost:3000/cars')
    if len(get_reply.text) == 2:
        print('*** Database is empty ***')
    elif len(get_reply.text) > 2:
        print(get_reply.text)


def delete_car():
    """asks user for car's ID and tries to delete it from database;"""
    car_id = input("Car ID (empty string to exit): ")
    del_reply = requests.delete(f'http://localhost:3000/cars/{car_id}')
    if del_reply.status_code == 200:
        print("Success")
    else:
        print(f"Request falls with status: {del_reply.status_code}")


def input_car_data():
    """
    lets user enter car data;
    argument determines if the car's ID is entered (True) or not (False);
    returns None if user cancels the operation or a dictionary of the following structure:
    {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }
    """
    id = input("Car ID (empty string to exit): ")
    brand = input("Car brand (empty string to exit): ")
    model = input("Car model (empty string to exit): ")
    prod_year = input("Car production year (empty string to exit): ")
    convertible = input("Is this car convertible? [y/n] (empty string to exit): ")
    if id is None:
        return None
    else:
        return {'id': id,
                'brand': brand,
                'model': model,
                'production_year': prod_year,
                'convertible': convertible}


def add_car():
    """invokes input_car_data(True) to gather car's info and adds it to the database;"""
    new_car = input_car_data()
    print(new_car)
    h_content = {'Content-Type': 'application/json'}
    post_reply = requests.post('http://localhost:3000/cars',
                               headers=h_content,
                               data=json.dumps(new_car))
    print(post_reply.status_code)


def update_car():
    """invokes enter_id() to get car's ID if the ID is present in the database;
    invokes input_car_data(False) to gather new car's info and updates the database;"""
    h_content = {'Content-Type': 'application/json'}
    put_car = input_car_data()
    car_id = put_car['id']

    put_reply = requests.put(f'http://localhost:3000/cars/{car_id}',
                             headers=h_content, data=json.dumps(put_car))
    if put_reply.status_code == 200:
        print("Success")
    else:
        print(f"Request falls with status: {put_reply.status_code}")


while True:
    if not check_server():
        print("Server is not responding - quitting!")
        exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars()
    elif choice == '2':
        add_car()
    elif choice == '3':
        delete_car()
    elif choice == '4':
        update_car()
