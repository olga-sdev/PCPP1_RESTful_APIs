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


def print_car(cars):
    """prints one car's data in a way that fits the header;
    id        | brand          | model     | production_year     | convertible    |
    1         | Porsche        | 911       | 1963                | False          |
    2         | Ford           | Mustang   | 1972                | True           |
    """
    '''reply = requests.get('http://localhost:3000/cars')
    cars = reply.json()'''
    print(
        'id    | brand      | model      | production_year | convertible |'
    )
    for car in cars:
        print(
            f'{car['id']:<5} | {car['brand']:<10} | {car['model']:<10} | {car['production_year']:<15} | {car['convertible']:<11} |'
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
        print_car(get_reply.json())


def name_is_valid(name):
    """
    checks if name (brand or model) is valid;
    valid name is non-empty string containing
    digits, letters;
    returns True or False;
    """
    for char in name:
        if char.isdigit() or char.isalpha() or char.isspace():
            return True
    else:
        return False


def enter_id(car_id):
    """
    allows user to enter car's ID and checks if it's valid;
    valid ID consists of digits only;
    returns int or None (if user enters an empty line);
    """
    try:
        if isinstance(car_id, int):
            return car_id
    except ValueError:
        return '-'


def enter_production_year(prod_year):
    """
    allows user to enter car's production year and checks if it's valid;
    valid production year is an int from range 1900..2000;
    returns int or None  (if user enters an empty line);
    """
    try:
        if int(prod_year) in range(1900, 2000):
            return int(prod_year)
    except ValueError:
        return '-'


def enter_name(what):
    """
    allows user to enter car's name (brand or model) and checks if it's valid;
    uses name_is_valid() to check the entered name;
    returns string or None  (if user enters an empty line);
    argument describes which of two names is entered currently ('brand' or 'model');
    """
    if name_is_valid(what):
        return str(what)
    else:
        return '-'


def enter_convertible(convertible):
    """allows user to enter Yes/No answer determining if the car is convertible;
    returns True, False or None  (if user enters an empty line);"""
    if convertible == 'n':
        return 'False'
    elif convertible == 'y':
        return 'True'
    else:
        return '-'


def delete_car():
    """asks user for car's ID and tries to delete it from database;"""
    car_id = input("Car ID (empty string to exit): ")
    del_reply = requests.delete(f'http://localhost:3000/cars/{car_id}')
    if del_reply.status_code == requests.codes.ok:
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
    car_id = input("Car ID (empty string to exit): ")
    #car_id = enter_id(car_id)
    brand = input("Car brand (empty string to exit): ")
    brand = enter_name(brand)
    model = input("Car model (empty string to exit): ")
    model = enter_name(model)
    prod_year = input("Car production year (empty string to exit): ")
    prod_year = enter_production_year(prod_year)
    convertible = input("Is this car convertible? [y/n] (empty string to exit): ")
    convertible = enter_convertible(convertible)
    if car_id is None:
        return None
    else:
        return {'id': car_id,
                'brand': brand,
                'model': model,
                'production_year': prod_year,
                'convertible': convertible}


def add_car():
    """invokes input_car_data(True) to gather car's info and adds it to the database;"""
    new_car = input_car_data()
    h_content = {'Content-Type': 'application/json'}
    post_reply = requests.post('http://localhost:3000/cars',
                               headers=h_content,
                               data=json.dumps(new_car))
    if post_reply.status_code == 200:
        print("Success")
    else:
        print(f"Request falls with status: {post_reply.status_code}")


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


"""
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
Car brand (empty string to exit): Ford
Car model (empty string to exit): -
Car production year (empty string to exit): 1971
Is this car convertible? [y/n] (empty string to exit): y
Request falls with status: 201
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
id    | brand      | model      | production_year | convertible |
1     | Ford       | -          | 1971            | True        |
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

Enter your choice (0..4): 4
Car ID (empty string to exit): 1
Car brand (empty string to exit): -
Car model (empty string to exit): Ford
Car production year (empty string to exit): 1987
Is this car convertible? [y/n] (empty string to exit): n
Success
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
id    | brand      | model      | production_year | convertible |
1     | -          | Ford       | 1987            | False       |
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
Success
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
Car brand (empty string to exit): Ford
Car model (empty string to exit): Galaxie
Car production year (empty string to exit): 1961
Is this car convertible? [y/n] (empty string to exit): y
Request falls with status: 201
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
id    | brand      | model      | production_year | convertible |
1     | Ford       | Galaxie    | 1961            | True        |
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

Process finished with exit code 0
"""
