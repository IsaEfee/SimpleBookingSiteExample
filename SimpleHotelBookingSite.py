admin_password = "admin123"
pass_attempts = 3

print("Welcome to Medipol Hotel Management System")

# Admin and Manager Login
while pass_attempts > 0:
    print("1. Admin Login")
    print("2. Manager Login")
    login_choice = input("Choose login type (1 for Admin, 2 for Manager): ")

    if login_choice == "1":
        print("Please enter the admin password to continue.")
        while pass_attempts > 0:
            Type_Password = input("Enter admin password: ")
            if Type_Password == admin_password:
                print("Password is correct. Welcome, Admin!")
                break
            else:
                pass_attempts -= 1
                print(f"Wrong password. Only {pass_attempts} attempts left.")
        else:
            print("Access denied. Exiting the system.")
            exit()
        break

    elif login_choice == "2":
        print("Please enter manager credentials to continue.")
        while pass_attempts > 0:
            username = input("Enter manager username: ")
            password = input("Enter manager password: ")

            if username in manager_names and manager_names[username] == password:
                print(f"Welcome, Manager {username}!")
                break
            else:
                pass_attempts -= 1
                print(f"Invalid credentials. Only {pass_attempts} attempts left.")
        else:
            print("Access denied. Exiting the system.")
            exit()
        break

    else:
        print("Invalid choice. Please type 1 or 2.")

# Menu Part
manager_names = {}
customer_history = {}

def menu():
    while True:
        print('1. Add/Remove Manager')
        print('2. Access Hotel Room Management System')
        print('3. Exit')
        choose = input('Make your choice (1-3): ')

        if choose == '1':
            manager_edit_menu()
        elif choose == '2':
            hotel_room_management()
        elif choose == '3':
            print('Goodbye! Thank you for using Medipol Hotel Management System.')
            break
        else:
            print('Invalid value. Please type again!')

# Manager edit part
def manager_edit_menu():
    while True:
        print('1. Add manager')
        print('2. Remove manager')
        print('3. Exit and return to Admin menu')
        select = input('Make your choice (1-3): ')

        if select == '1':
            username = input('Enter manager username: ')
            password = input('Enter manager password: ')
            if username in manager_names:
                print('Name is already taken')
            else:
                manager_names[username] = password
                print(f'Manager {username} has been added successfully.')
        elif select == '2':
            username = input('Enter the username of the manager to remove: ')
            if username in manager_names:
                del manager_names[username]
                print(f'Manager {username} has been removed successfully.')
            else:
                print(f'There is no manager named {username}.')
        elif select == '3':
            break
        else:
            print('Invalid value. Please type again.')

# Hotel room management part
def hotel_room_management():
    rooms = {
        640: {"type": "Single", "price": 2350, "status": "Available"},
        641: {"type": "Double", "price": 3500, "status": "Booked"},
        642: {"type": "Deluxe", "price": 7200, "status": "Available"},
    }

    def room_menu():
        print("1. Add Room")
        print("2. Remove Room")
        print("3. Search a Room")
        print("4. Booking for Rooms")
        print("5. Generate Report")
        print("6. Show customer history")
        print("7. Exit")

    def add_rooms():
        room_number = int(input("Enter Room Number: "))
        if room_number in rooms:
            print(f"Room {room_number} already exists.")
        else:
            room_type = input("Type room type (Single, Double, Deluxe): ")
            price = int(input("Enter Price: "))
            rooms[room_number] = {"type": room_type, "price": price, "status": "Available"}
            print(f"Room {room_number} added successfully.")

    def remove_rooms():
        room_number = int(input("Which room do you want to delete?: "))
        if room_number in rooms:
            del rooms[room_number]
            print(f"Room {room_number} deleted successfully.")
        else:
            print(f"Room {room_number} couldn't be found.")

    def booking_rooms():
        room_number = int(input("Enter room number: "))
        if room_number in rooms:
            if rooms[room_number]["status"] == "Available":
                name = input("Enter your name: ")
                stay_period = input("Enter your stay period (e.g., 2024-12-20 to 2024-12-25): ")
                rooms[room_number]["status"] = "Booked"
                customer_history[name] = {"room": room_number, "stay_period": stay_period}
                print(f"Room {room_number} booked for {name} from {stay_period}.")
            else:
                print(f"Room {room_number} is already booked.")
        else:
            print(f"Room {room_number} does not exist.")

    def search_rooms():
        room_type = input("Enter Room Type (Single/Double/Deluxe): ")
        min_price = int(input("Enter Minimum Price: "))
        max_price = int(input("Enter Maximum Price: "))
        status = input("Enter Room Status (Available/Booked): ")

        matching_rooms = []
        for room_number, details in rooms.items():
            if (details["type"] == room_type and 
                min_price <= details["price"] <= max_price and 
                details["status"] == status):
                matching_rooms.append(room_number)

        if matching_rooms:
            print(f"Matching Rooms: {', '.join(map(str, matching_rooms))}")
        else:
            print("No matching rooms found.")

    def generate_report():
        available_rooms = len([r for r in rooms.values() if r["status"] == "Available"])
        booked_rooms = len([r for r in rooms.values() if r["status"] == "Booked"])
        total_revenue = sum(r["price"] for r in rooms.values() if r["status"] == "Booked")

        print(f"Available Rooms: {available_rooms}")
        print(f"Booked Rooms: {booked_rooms}")
        print(f"Total Revenue: ${total_revenue}")

    def show_customer_history():
        if not customer_history:
            print("No customer history available.")
        else:
            for name, details in customer_history.items():
                print(f"Customer: {name}, Room: {details['room']}, Dates: {details['stay_period']}")

    while True:
        room_menu()
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            add_rooms()
        elif choice == "2":
            remove_rooms()
        elif choice == "3":
            search_rooms()
        elif choice == "4":
            booking_rooms()
        elif choice == "5":
            generate_report()
        elif choice == '6':
            show_customer_history()
        elif choice == "7":
            print("Returning to Admin menu")
            break
        else:
            print("Invalid value. Please type again.")



while pass_attempts > 0:
    print("1. Admin Login")
    print("2. Manager Login")
    login_choice = input("Choose login type (1 for Admin, 2 for Manager): ")

    if login_choice == "1":
        print("Please enter the admin password to continue.")
        while pass_attempts > 0:
            Type_Password = input("Enter admin password: ")
            if Type_Password == admin_password:
                print("Password is correct. Welcome, Admin!")
                break
            else:
                pass_attempts -= 1
                print(f"Wrong password. Only {pass_attempts} attempts left.")
        else:
            print("Access denied. Exiting the system.")
            exit()
        break

    elif login_choice == "2":
        print("Please enter manager credentials to continue.")
        while pass_attempts > 0:
            username = input("Enter manager username: ")
            password = input("Enter manager password: ")

            if username in manager_names and manager_names[username] == password:
                print(f"Welcome, Manager {username}!")
                hotel_room_management()
            else:
                pass_attempts -= 1
                print(f"Invalid credentials. Only {pass_attempts} attempts left.")
        else:
            print("Access denied. Exiting the system.")
            exit()
        break

    else:
        print("Invalid choice. Please type 1 or 2.")
menu()
