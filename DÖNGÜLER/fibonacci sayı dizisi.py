# fibonacci sayı dizisi

"""
Fibonacci Serisi yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur.
1,1,2,3,5,8,13,21,34...............
"""

a= 1
b= 1

x = int(input("kaç elemanlı olsun: "))

fibonacci = [a,b]

for i in range(x-2):
    a,b = b,a+b # çok önemli
    fibonacci.append(b)

print(fibonacci)

