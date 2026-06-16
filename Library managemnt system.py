books = []

while True: 
    print("\n=== libaray management system ===")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice")

    #1. Add Book 

    if choice == "1": 
        title = input("Enter your book title: ")
        author = input("Enter author name: ")

        book = {
            "title":title,
            "author":author,
            "available":True

        }

        books.append(book)
        print("Book added sucessfully!")

    #2. View Books 

    elif choice == "2":
        if len(books) == 0: 
            print("No books available. ")

        else:
            for book in books:
                status = "Available" if book["available"] else "borrowed"
                print(f"{book['title']} by {book['author']} - {status}")


    #3. Search books 

    elif choice == "3":
        search = input("Enter book title: ")

        for book in books:
            if book["title"].lower() == search.lower():
                print(f"found:{book['title']} by {book[author]}")
                break

            else:
                print("Book not found")

    #4. Borrow books  
    elif choice == "4":
        borrow = input("Enter book title to borrow") 

        for book in books:
            if book ["title"].lower() == borrow.lower():
                if book["available"]:
                  book ["available"] = False
                print("Book borrowed sucessfully  ")  
                break 

            else:
                print("Book is already borrowed") 

    #5. Return Books 

    elif choice == "5":
        return_book = input("Enter book title to return")

        for book in books:
            if book["title"].lower() == return_book.lower():
                book["available"] = True 
                print("Book returned successfullly")
                break 

        else:
           print("Book is not found")


    #6. Exit 
    elif choice == "6":
        print("Goodbye!")
        break 

    else:
        print("Invalid choice")




