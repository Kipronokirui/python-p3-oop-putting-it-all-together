#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count): 
        self.title = title 
        self.page_count = page_count 
    
    def show_book_title(self, newTitle):
        self.title =  newTitle  
        print('The book title is:', self.title)

    def show_page_count(self):   
        print('The book page count is:', self.page_count)

title = Book("Manchester United", 23)
title.show_book_title("Chelsea")
    
        