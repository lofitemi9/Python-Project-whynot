from tkinter import*
import tkinter

root = Tk(screenName=None, baseName=None, className='App', useTk=1)
#Main loop (IMPORTANT)
main = tkinter.Tk()

# -------------------------------------------------------------------
# menu for the budgeting app
print('''
      
      1. View Categories
      2. Add Category
      3. Delete Category
      4. Exit
      
      ''')

# creating an empty list to hold all the categories
categories = []

choice = input("Pick a Number 1 - 4")

def addCategory():
    newCategory = input("What do you want to add ?: ")
    categories.insert(newCategory)
    
def viewCategories():
    print('''

    ''')
    
    
def delCategory():
    pass


if choice == "1":
    viewCategories()
elif choice == "2":
    addCategory()
elif choice == "3":
    delCategory()

#Add 



























#MAIN LOOP (IMPORTANT!!!!!!!)
main.mainloop()
