#"""LOOPS"""

# 1. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a nested loop.
# Օգտագործելով ցիկլեր, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

#matrix = []
#temp = []
#n = 0

#for i in range(1,10):
#    temp.append(i ** 2)
#    n += 1

#    if n == 3 :
#        matrix.append(temp)
#        temp = []
#        n = 0
#print(matrix)
#
# 2. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a list comprehension.
# Օգտագործելով comprehension, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։
#
# lst = [[((j + 1) + i *3)**2 for j in range(3)] for  i in range(3)]
# print(lst)
#
#
# 4. Count the number of 'b's in the given string. DO NOT use the count() method.
# Հաշվել տրված սթրինգում 'b'-երի քանակը։ Չօգտագործել count() մեթոդը։

# nonsense = 'Blinking blindly, brainy Bob brings beautiful beer bottles beneath blue butterflies billowing brilliantly.'
#
# total = 0
#
# for char in nonsense.lower():
#     if char =='b':
#         total += 1
# print(total)

# # 5. Write a program that will print the factorial of n.
# # Գրել ծրագիր, որը կտպի n թվի ֆակտորիալը։
#
# n = int(input('Enter a number :'))
# result = n
#
# for i in range(1, n):
#     result *= i
#
# print(result)




