# ============================================================
# MAGIC / DUNDER METHODS — Challenge 1
# __repr__ and __str__
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
    
    
book1 = Book("Dune", "Frank Herbert", 412)

print(repr(book1))
print(book1)