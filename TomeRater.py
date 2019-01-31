class User():
    '''
    This is a User class that takes 2 strings  
    name, email as 'string'  
    the available methods are read_book, get_average_rating
    '''

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {} #this is a dictionary of Book:rating(int) 

    def get_email(self):
        return self.email

    def change_email(self, address):
        print (f"{self.name}'s email address has changed from {self.email} to {address}")
        self.email = address

    def read_book(self, book, rating = None):
        '''this takes book as Book & rating as (int) from 0 to 4'''
        self.books[book] = rating

    def get_average_rating(self):
        total_rating = 0
        for book in self.books.keys():
            total_rating += self.books[book]
        return (total_rating/len(self.books.keys()))

    def __repr__(self):
        return "User: {self.name}, email: {self.email}, books read: {}".format(**locals())

    def __eq__(self, other_user):
        '''this implements the comparison operator == to check if the user name, email are the same as another user'''
        if type(self) != User and type(other_user) != User:
            return "both objects are not User class objects"
        else:
            return self.name == other_user.name and self.email == other_user.email

class Book():
    '''
    this is a book Class that takes 2 arguments  
    title as 'string' & isbn as (int)  
    the available methods are  
    set_isbn(new_isbn), add_rating, get_average_rating
    '''
    
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        print (f"the book {self.title}'s ISBN has been updated\nfrom {self.isbn} to {new_isbn}")
        self.isbn = new_isbn

    def add_rating(self, rating):
        '''takes rating as (int) from 0 to 4 & appends to rating list'''
        if rating is int and rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print ("Invalid Rating\nPlease choose an integer from 0 to 4")

    def get_average_rating(self):
        total_rating = 0
        for rating in self.ratings:
            total_rating += rating
        return (total_rating/len(self.ratings))
    
    def __eq__(self, other_book):
        '''this implements the comparison operator == to check if the title, isbn are the same as another book'''
        if type(self) != Book and type(other_book) != Book:
            return "both objects are not Book class objects"
        else:
            return self.title == other_book.title and self.isbn == other_book.isbn

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    '''
    this is a Book subclass that takes 3 arguments  
    title, author as 'string' & isbn as (int)
    '''
    
    def __init__(self, title, author, isbn):
        super().__init__(self, title, isbn)
        self.author = author

    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{self.title} by {self.author}".format(**locals())

class Non_Fiction(Book):
    '''
    this is a Book subclass that takes 4 arguments  
    title, subject(ex. biology), level(ex begginer) as 'string' & isbn as (int)
    '''

    def __init__(self, title, subject, level, isbn):
        super().__init__(self, title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{self.title}, a {self.level} manual on {self.subject}".format(**locals())

class TomeRater():
    '''
    This is the main class to track users, books read, & ratings  
    the available methods are  
    create_book, create_novel, create_non_fiction, add_book_to_user, add_book_to_user, print_catalog, print_users, most_read_book, most_positive_user
    '''

    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        '''takes a title as 'string' & isbn as (int)'''
        return Book(title, isbn)
    
    def create_novel(self, title, author, isbn):
        '''takes a title, author as 'string' & isbn as (int)'''
        return Fiction(title, author, isbn)
    
    def create_non_fiction(self, title, subject, level, isbn):
        '''takes title, subject, level as 'string' & isbn as (int)'''
        return Non_Fiction(title, subject, level, isbn)
    
    def add_book_to_user(self, book, email, rating = None):
        '''takes book as Book, email as 'string' & optional rating as (int) from 0 to 4  
        adds book:rating to books dict'''
        if email not in self.users.keys():
            print (f"No user with email {email}!")
        else:
            self.users[email].read_book(book, rating)
        
        if book not in self.books.keys():
            self.books[book] = 1
        else:
            self.books[book] += 1

    def add_user(self, name, email, user_books = None):
        '''takes name, email as 'string', & optional list of books as Book  
        adds email:User(name, email) to users dict'''
        self.users[email] = User(name, email)
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)
        else:
            pass
    
    def print_catalog(self):
        for book in self.books.keys():
            print (book.get_title())
    
    def print_users(self):
        for email in self.users.keys():
            print (email.name)
    
    def most_read_book(self):
        max_read = max(self.books.values())
        for book in self.books.keys():
            #returns book if it is == most read value 
            if self.books[book] == max_read:
                return book
    
    def highest_rated_book(self):
        best_rating = 0 #score place holder
        for book in self.books.keys():
            #sets highest avg rated book as returned book
            if book.get_average_rating() > best_rating:
                best_book = book
        return best_book
    
    def most_positive_user(self):
        most_positive = 0 #score place holder
        for user in self.users.keys():
            #sets highest avg score to returned user
            if user.get_average_rating > most_positive: 
                positive_user = user
        return positive_user
