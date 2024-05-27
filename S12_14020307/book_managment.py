from tools import *
from book import Book

class BookManagment:
    def BookID():
        with open("S12_14020307\\DB\\last_book_id.txt","r") as file:
            lastBookId = file.read()
            if lastBookId != "":
                lastBookId = int(lastBookId) + 1
                return lastBookId
            else:
                return 1
    
    def UpdateLastBookID():
        lastBookId = BookManagment.BookID()
        with open("S12_14020307\\DB\\last_book_id.txt","w") as file:
            file.write(str(lastBookId))

    def AddBook():
        ClearTerminal()
        print(ColoredNotification("Add Book", "green"))
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        year = input("Enter Book published Year: ")
        selectedBook = Book(BookManagment.BookID(),title, author, year)
        with open("S12_14020307\\DB\\books.txt","a") as file:
            file.write(f"{selectedBook.__dict__}\n")
            file.close()
        BookManagment.UpdateLastBookID()

    def ShowBooks():
        ClearTerminal()
        print(ColoredNotification("Books List", "green"))
        with open("S12_14020307\\DB\\books.txt","r") as file:
            for line in file.readlines():
                currentBookDict = eval(line)
                selectedBook = Book(currentBookDict['id'],currentBookDict['title'],currentBookDict['author'],currentBookDict['year'])
                #selectedBook = Book(**eval(line.strip()))
                print(f"{selectedBook.id} | {TextStructure(selectedBook.title,20)}| {TextStructure(selectedBook.author,30)}| {selectedBook.year}")

    booksList = []

    def UpdateBooksList():
        BookManagment.booksList = []
        with open("S12_14020307\\DB\\books.txt","r") as file:
            for line in file.readlines():
                BookManagment.booksList.append(eval(line))

    def UpdateBooksTxt():
        with open("S12_14020307\\DB\\books.txt","w") as file:
            for book in BookManagment.booksList:
                file.writelines(f"{book}\n")

    def SearchBook():
        ClearTerminal()
        BookManagment.UpdateBooksList()
        print(ColoredNotification("Search Book", "green"))
        bookId = input("Please Enter the Book ID: ")
        for book in BookManagment.booksList:
            if book['id'] == int(bookId):
                print(f"Book ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Year: {book['year']}")

    def EditBook():
        ClearTerminal()
        BookManagment.UpdateBooksList()
        print(ColoredNotification("Edit Book", "green"))
        bookId = input("Please Enter the Book ID: ")
        for book in BookManagment.booksList:
            if book['id'] == int(bookId):
                print(f"Book ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Year: {book['year']}")
        bookTitle = input("Please Enter the NEW Book Title: ")
        bookAuthor = input("Please Enter the NEW Book Author: ")
        bookYear = input("Please Enter the NEW Book Year: ")
        for index, book in enumerate(BookManagment.booksList):
            if book['id'] == int(bookId):
                selectedBook = Book(int(bookId), bookTitle, bookAuthor, bookYear)
                BookManagment.booksList[index] = selectedBook.__dict__
        BookManagment.UpdateBooksTxt()
        

    def DeleteBook():
        ClearTerminal()
        BookManagment.UpdateBooksList()
        print(ColoredNotification("Delete Book", "green"))
        bookId = input("Please Enter the Book ID: ")
        for index, book in enumerate(BookManagment.booksList):
            if book['id'] == int(bookId):
                BookManagment.booksList.pop(index)
        BookManagment.UpdateBooksTxt()