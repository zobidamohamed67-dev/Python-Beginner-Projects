library = []
wishlist = []

book1 = input("Enter the name of a book you own:\n")
library.append(book1)

book2 = input("Enter the name of another book you own (or press enter to skip)\n")
if book2:
    library.append(book2)
    print("Your library:", library)
else:
    print("Your library is:", library)

wish1 = input("Enter the name of a book you wish to have:\n")
wishlist.append(wish1)

wish2 = input("Enter the name of another book you wish to have (or press enter to skip)\n")
if wish2:
    wishlist.append(wish2)
    print("Your wishlist is:", wishlist)
else:
    print("Your wishlist is:", wishlist)

book_acquired = input("Enter the name of a book of your wishlist you've already acquired (or press enter to skip)\n")
if book_acquired:
    if book_acquired in wishlist:
        library.append(book_acquired)
        wishlist.remove(book_acquired)
        print("Updated library:", library)
        print("Updated wishlist:", wishlist)
    else:
        print("Book not found in wishlist.")

don = input("Enter the name of a book of your library you want to donate (or press enter to skip)\n")
if don:
    if don in library:
        library.remove(don)
        print("Your final library after donation:", library)
    else:
        print("Book not found in library.")
else:
    print("Your final library is:", library)
