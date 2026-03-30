

import os
books={}
def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")


while True:
    print("""
Menu:
1- Add Book
2- Check out Book
3- Check In Book
4- List Books
5-Exit""")
    
    choise=int(input("Enter your choice (1 - 5):\n"))
    clear()
    if choise== 1:
        while True:
          num=int(input("Enter ISBN: "))
          title=input("Enter title: ")
          auth=input("Enter auther:")


          books[num]={
              "title":title,
              "author":auth,
              "is_avilable":True,
          }

          print(f"Book '{books[num]['title']}' by {books[num]['author']} added to the catalog with ISBN {num}")

          add_more=input("DO you want to add another book? (y/n): ").lower()
          clear()

          if add_more=="n":
              
              break
    
    elif choise== 2 :
        num= int(input("Please enter the ISBN of the  book you want to check out: \n"))

        if num in books:
            if books[num]["is_avilable"]==True:
                books[num]["is_avilable"] = False
                print(f"Success! You have checked out '{books[num]['title']}'.")

            else:
                print(f"Sorry,{books[num]['title']} is already checked out by someone else .")
        else:
            print("Sorry we do not have this book on our library...")

        input("Press enter to go to the main menu....")
        clear()
    
    elif choise == 3 :
        num= int(input("Please enter the ISBN you want to check in: \n"))
        if num in books:
            if books[num]["is_avilable"]==False:
                books[num]["is_avilable"] = True
                print(f"Success! You have checked in '{books[num]['title']}'.")
            
            else:
                print(f"{books[num]['title']} is already checked in.")
        
        else:
            print("Sorry but this book not from our library...")

        input("Press enter to go to the main menu.....")

    elif choise == 4:
        print("\n--- Library Catalog ---")
        if len(books) == 0:
            print("The library is currently empty.")
        else:
            for isbn, details in books.items():
                status = "Available" if details["is_avilable"] else "Checked Out"
                print(f"ISBN: {isbn} | Title: {details['title']} | Author: {details['author']} | Status: {status}")
                
        input("\nPress enter to return to the main menu...")
        clear()

    elif choise == 5:
        clear()
        print("EXITING........")
        break

    else:
        print("Invalid choise please choose from 1-5")
        input("Press enter to go to the main menu....")
        clear()
