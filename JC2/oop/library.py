class Library:
    def __init__(self,name):
        self.__name = name
        self.__book = [] #declare array
    
    def getName(self):
        return self.__name
    def getBook(self):
        return self.__book

    def setName(self, newName):
        self.__name = newName
    
    def addBook(self,books): #whatever book object passed will be now added into the array
        self.__book.append(books)
    
    def printBooks(self):
        for book in self.__book: #for every book object in this array
            print (f"Title: {book.getTitle()} , Author: {book.getAuthor()}, Price: {book.getPrice()}")
    

        
class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price
    
    def getTitle(self):
        return self.__title
    def getAuthor(self):
        return self.__author
    def getPrice(self):
        return self.__price
    

bbsLibrary = Library("Bina Bangsa School Library")
book1 = Book("Cambridge ALevel CS", "Cambridge", 1000) #immediately an object and not a class anymore
book2 = Book("Hunger Games", "Suzanne Collins", 300)
bbsLibrary.addBook(book1) #passing an object inside the c;ass

bbsLibrary.printBooks()
