'''
Created on Nov 4, 2017

@author: arnon
'''
import os
from acrilib import find_meta, read_authors, read_meta_or_file

if __name__ == '__main__':
    text = find_meta('authors', 'test__init__01.py', error=True)
    print(read_authors(text))

    text = read_meta_or_file('authors', 'test__init__01.py', )
    print(read_authors(text))

    text = read_meta_or_file('authors', 'test__init__02.py',
                             file=os.path.dirname(__file__))
    print(read_authors(text))
