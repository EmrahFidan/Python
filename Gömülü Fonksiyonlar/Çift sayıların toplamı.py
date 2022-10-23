"""
Elinizde şöyle bir liste bulunsun.

    [1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.
"""

def even(x):
    if(x%2==0):
        return x

def sum(x,y):
    return x+y

from functools import reduce

list1 = [1,2,3,4,5,6,7,8,9,10]

list2 = list(filter(even,list1))

print(reduce(sum,list2))
