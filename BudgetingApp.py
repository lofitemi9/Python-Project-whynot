# from tkinter import*
# import tkinter

# root = Tk(screenName=None, baseName=None, className='App', useTk=1)
# #Main loop (IMPORTANT)
# main = tkinter.Tk()

# -------------------------------------------------------------------
# menu for the budgeting app
print('''
      
      1. View Categories
      2. Add Category
      3. Delete Category
      4. Exit
      
      ''')
# -------------------------------------------------------------------
# creating an empty list to hold all the categories
categories = []

#prompting the user to select a choice on the menu
choice = int(input("Pick a Number 1 - 4: \n"))


def addCategory():#It adds a Category that the user wants
    works = True
    while works:
        newCategory = input("What do you want to add ?: ")
        categories.append(newCategory)
        more = input("Do you wanna add more (y/n)")
        if more == 'n': 
            works = False

        print(categories)
    
def viewCategories(): #So like lists out the categories
    print("These are your Categories: ")
    with open("Expenses.csv", "r") as file:
        for line in file:
            category = line.strip().split(',')
            if category != "":
                print(category)
            

def delCategory():#deletes a category
    print("Select a category to delete: ")
    for category in categories:
        print(category)


match choice:
    case 1: viewCategories()
    case 2: addCategory()
    case 3: delCategory()
    case 4: exit
    


#Creating and saving user category
with open("Expenses.csv", "a") as file:
    for category in categories:  #Logic for the category names, so that we can see them
        file.write(f", {category} ")

        if(category != categories[-1]):
            file.write(f",")



















#MAIN LOOP (IMPORTANT!!!!!!!)
#main.mainloop()



