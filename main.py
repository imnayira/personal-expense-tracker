def view_expenses(data):
    for item in data:
        print(f"ID: {item["id"]}\nCategory: {item["category"]}\nDescription: {item["description"]}\nAmount: {item["amount"]}\nDate: {item["date"]}")
        print("--------------------------------------------------------")

def add_expense(data, id, category, description, amount, date):
    if search_by_id(data, id) is None:
        new_expense = {"id":id, "category":category, "description":description, "amount":amount, "date":date}
        data.append(new_expense)
    else:
        print("ID already exists, try again!")

def search_by_category(data, category):
    items_in_category = []
    for item in data:
        if item["category"] == category:
            items_in_category.append(item)
    return items_in_category

def search_by_id(data, id):
    for item in data:
        if item["id"] == id:
            found = f"ID: {item["id"]}\nCategory: {item["category"]}\nDescription: {item["description"]}\nAmount: {item["amount"]}\nDate: {item["date"]}"
            return found
    return None

def delete_expense(data, id):
    item_to_be_deleted = search_by_id(data, id)
    if item_to_be_deleted is not None:
        data.remove(item_to_be_deleted)
    else:
        print("Item not found")

def total_spending(data):
    total = 0
    for item in data:
        total+=item["amount"]
    return total

def save_expenses(data, file):
    with open(file, "w") as file:
        for item in data:
            line = f"{item["id"]},{item["category"]},{item["description"]},{item["amount"]},{item["date"]}"
            file.write(line+"\n")


def load_expenses(file):
    expenses = []
    with open(file, "r") as file:
        for line in file:
            part=line.strip().split(",")
            expense = {"id":int(part[0]), "category":part[1], "description":part[2], "amount":int(part[3]), "date":part[4]}
            expenses.append(expense)
    return expenses

def print_search(found):
    print(f"ID: {found["id"]}\nCategory: {found["category"]}\nDescription: {found["description"]}\nAmount: {found["amount"]}\nDate: {found["date"]}")

def main_menu():
    print("""-----Check the options below-----
1- View all expenses
2- Add a new expense
3- Delete an expense
4- View total spendings
5- Search for an expense
6- Exit
          """)
    
def search_menu():
    print("""1- Search by ID
2- Search by Category
3- Back
          """)
    

file_ = "expenses.txt"
expenses = load_expenses(file_)


while True:
    main_menu()
    choice = input("Enter your choice [1-6] : ")

    if choice == "1":
        view_expenses(expenses)

    elif choice == "2":
        try:
            id_of_new_expense = int(input("Enter the ID: "))
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            amount = int(input("Enter the amount: "))
            date = input("Enter the date [dd-mm-yyyy]: ")
            add_expense(expenses, id_of_new_expense, category, description, amount, date)
            save_expenses(expenses, file_)
        
        except ValueError:
            print("Invalid input")
     
    elif choice == "3":
        try:
            id_to_be_deleted = int(input("Enter the ID of the item you want to delete: "))
            delete_expense(expenses, id_to_be_deleted)
            save_expenses(expenses, file_)
        except ValueError:
            print("Invalid input!")

        
    elif choice == "4":
        print(f"total spendings: {total_spending(expenses)}\n")

    elif choice =="5":
        search_menu()
        search_choice = input("Enter your choice: ")
        if search_choice == "1":
            try:
                search_id = int(input("Enter the ID: "))
                print(search_by_id(expenses, search_id))
            except ValueError:
                print("Invalid input!")
                
        elif search_choice == "2":
            search_category = input("Enter the category: ")
            search_by_category(expenses, search_category)