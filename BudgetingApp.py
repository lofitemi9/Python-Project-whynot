print("""
1. View Categories
2. Add Category
3. Delete Category
4. Exit
""")

categories = []

try:
    choice = int(input("Pick a Number 1 - 4: "))
except:
    print("Invalid input")
    exit()

def addCategory():
    while True:
        newCategory = input("What do you want to add?: ")
        categories.append(newCategory)
        more = input("Add more? (y/n): ")
        if more.lower() == "n":
            break

def viewCategories():
    print("These are your Categories:")
    try:
        with open("Expenses.csv", "r") as file:
            for line in file:
                cats = [c.strip() for c in line.split(",") if c.strip()]
                for c in cats:
                    print("-", c)
    except FileNotFoundError:
        print("No categories yet.")

def delCategory():
    delCat = input("Select a category to delete: ").lower()
    try:
        with open("Expenses.csv", "r") as file:
            content = file.read()
        cats = [c.strip() for c in content.split(",") if c.strip()]
        if delCat not in [c.lower() for c in cats]:
            print("That category doesn't exist.")
            return
        if input("Delete? (y/n): ") == "y":
            cats = [c for c in cats if c.lower() != delCat]
            with open("Expenses.csv", "w") as file:
                file.write(",".join(cats))
            print("Deleted.")
    except FileNotFoundError:
        print("No file found.")

match choice:
    case 1: viewCategories()
    case 2: addCategory()
    case 3: delCategory()
    case 4: exit()

if categories:
    try:
        with open("Expenses.csv", "r") as file:
            existing = file.read()
            existing = [c.strip() for c in existing.split(",") if c.strip()]
    except FileNotFoundError:
        existing = []

    all_categories = existing + categories

    with open("Expenses.csv", "w") as file:
        file.write(",".join(all_categories))

