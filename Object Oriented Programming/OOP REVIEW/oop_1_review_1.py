# ============================================================
# OOP REVIEW — Topic 1: Classes, __init__, self, instance attributes
# Mehmet's Python Journey | Day 47
# ============================================================


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summery(self):
        print(f"[{self.title}] by [{self.author}] - [{self.pages}] pages")


book1 = Book('Bad Habits', 'Johny Clay', 260)
book2 = Book('Never Quit', 'David Gog', 1200)

book1.summery()
book2.summery()