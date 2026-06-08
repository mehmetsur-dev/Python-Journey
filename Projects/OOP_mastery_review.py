# ============================================================
# library_system.py
# OOP Mastery Project — Day 28
# Topics: Classes, Class Variables, @classmethod, @staticmethod,
#         Inheritance, super(), Dunder Methods, @property
# Author: Mehmet Sur
# Date: 2026-05-31
# ============================================================


class Book:
    total_books = 0

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        Book.total_books += 1

    @classmethod
    def from_string(cls, book_str):
        title, author, pages = book_str.split('-')
        return cls(title, author, int(pages))
    
    @staticmethod
    def is_valid_pages(pages):
        return isinstance(pages, int) and pages > 0
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @title.deleter
    def title(self):
        print(f"Deleting title: {self._title}")
        del self._title   

    def __repr__(self):
        return f"Book({self.title}, {self.author})"
    
    def __str__(self):
        return f"Book={self.title}, Author={self.author}"
    
    def __eq__(self, value):
        return self.title == value.title and self.author == value.author
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __add__(self, other):
        return int(self.pages + other.pages)


class EBook(Book):
    total_ebooks = 0

    def __init__(self, title, author, pages, file_size_mb):
        super().__init__(title, author, pages)
        if not isinstance(file_size_mb, (int, float)) or file_size_mb <= 0:
            raise ValueError("file_size_mb must be a positive number")
        self.file_size_mb = file_size_mb
        EBook.total_ebooks += 1

    def __str__(self):
        return f"Book={self.title}, Author={self.author}, Size={self.file_size_mb}"


class Library:
    def __init__(self, name, books=None):
        self.name = name

        if books is None:
            self.books = []
        else:
            self.books = books

    def add_book(self, book):
        return self.books.append(book)
    
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return
    
    def find_by_author(self, author):
        return [book for book in self.books if book.author == author]
    
    def __len__(self):
        return len(self.books)
    
    def __str__(self):
        return f"Library: {self.name}, Books: {len(self)}"
    
#--------------------
#       Test
#--------------------

if __name__ == "__main__":

    # Book + classmethod
    b1 = Book("The Hobbit", "Tolkien", 310)
    b2 = Book.from_string("Dune-Herbert-412")

    # __str__, __repr__
    print(b1)
    print(repr(b1))

    # __eq__, __lt__, __add__
    print(b1 == b2)
    print(b1 < b2)
    print(b1 + b2)

    # @staticmethod
    print(Book.is_valid_pages(310))
    print(Book.is_valid_pages(-5))

    # @property deleter
    del b1.title

    # EBook + isinstance check
    eb1 = EBook("Clean Code", "Martin", 431, 2.5)
    print(eb1)

    # total_books counter
    print(Book.total_books)
    print(EBook.total_ebooks)

    # Library
    lib = Library("City Library")
    lib.add_book(b2)
    lib.add_book(eb1)
    print(lib)
    print(len(lib))
    print(lib.find_by_author("Martin"))
    lib.remove_book("Dune")
    print(len(lib))