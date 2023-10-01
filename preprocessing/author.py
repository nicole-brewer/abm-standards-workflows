# AUTOGENERATED! DO NOT EDIT! File to edit: ../author.ipynb.

# %% auto 0
__all__ = ['Name', 'Author']

# %% ../author.ipynb 3
import pandas as pd
import pprint
import bisect

# %% ../author.ipynb 5
class Name(str):

    def __new__(cls, value):  
        if not value:
            value = ''
        obj = str.__new__(cls, value)
        return obj    
            
    def matches(self, other):
        return str(self) == str(other)
        
    def __eq__(self, other):
        if len(self) == 0 or len(other) == 0:
            return True
        elif len(self) == 1:
            if len(other) > 1:
                return str(other[0]).__eq__(self)
            else:
                return str(other).__eq__(self)
        else:
            if len(other) == 1:
                return str(self[0]).__eq__(other[0])
            else:
                return str(self).__eq__(other)
            
    def longest(self, other):
        if not self == other:
            raise Exception('cannot merge names that aren\'t equivalent')
        if len(other) > len(self):
            return other
        else:
            return self

# %% ../author.ipynb 15
class Author:
    
    def __init__(self, last, first, middle='', middle2='', middle3='', emails=[]):
        self.first = Name(first)
        self.middle = Name(middle)
        self.middle2 = Name(middle2)
        self.middle3 = Name(middle2)
        self.last = Name(last)
        self.emails = emails
        self.publications = []

    def full_name(self):
        strings = [getattr(self, attr) for attr in ('first', 'middle', 'middle2', 'middle3', 'last') if getattr(self, attr)]
        strings = list(filter(None, strings))
        strings = ' '.join(strings)
        return strings
        
    def __repr__(self):
        return self.full_name()
    
    def matches(self, other):
        return (self.first.matches(other.first)
            and self.middle.matches(other.middle)
            and self.middle2.matches(other.middle2)
            and self.middle3.matches(other.middle3)
            and self.last.matches(other.last))
    
    def add_contact_author_info(self, contact_author):
        # use the __eq__ function to make sure the author and contact_author are the same before merging them
        assert self.same_name(contact_author), 'author and contact_author do not have the same name'
        self.emails = self.emails + contact_author.emails
        self.merge_names(contact_author)
        
    def merge_names(self, other):
        self.first = self.first.longest(other.first)
        self.middle = self.middle.longest(other.middle)
        self.middle2 = self.middle2.longest(other.middle2)
        self.middle3 = self.middle3.longest(other.middle3)
        self.last = self.last.longest(other.last)

    def same_name(self, other):
        return (self.last, self.first, self.middle, self.middle2, self.middle3) == (other.last, other.first, other.middle, other.middle2, other.middle3)

    def __lt__(self, other):
        return (self.last, self.first, self.middle, self.middle2, self.middle3) < (other.last, other.first, other.middle, other.middle2, other.middle3)

    def __le__(self, other):
        return (self.last, self.first, self.middle, self.middle2, self.middle3) <= (other.last, other.first, other.middle, other.middle2, other.middle3)

    def __gt__(self, other):
        return (self.last, self.first, self.middle, self.middle2, self.middle3) > (other.last, other.first, other.middle, other.middle2, other.middle3)

    def __ge__(self, other):
        return (self.last, self.first, self.middle, self.middle2, self.middle3) >= (other.last, other.first, other.middle, other.middle2, other.middle3)
