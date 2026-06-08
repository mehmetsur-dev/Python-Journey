# ============================================================
# MAGIC / DUNDER METHODS — Challenge 2
# __add__ and __len__
# Day 26 — Mehmet Sur
# ============================================================


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"
    
    def __add__(self, other):
        return self.pages + other.pages
    
    def __len__(self):
        return self.pages
    
book1 = Book("Dune", "Frank Herbert", 412)
book2 = Book("1984", "George Orwell", 328)

print(book1 + book2)  
print(len(book1))     

print(repr(book1))
print(book1)