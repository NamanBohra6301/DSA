import string
import random
A=string.ascii_letters
n=int(input())
for i in range(n):
    L=[]
    for j in range(n):
        L.append(random.choice(A))

        for element in L:
            print(element,end=('\t'))
        print()
# L1=['harry potter','matrix','spiderman','avengers','john wick']
# L2=['drishyam','spiderman','bahubali','dhoom','race','matrix']
# L=[]
# for i in range(len(L1)):
#     flag=0
#     for j in range(len(L2)):
#         if(L1[i]==L2[j]):
#             flag=1
#             break
#         else:
#             flag=0
#     if(flag==0):
#         L.append(L1[i])
# print(L)
# print([i**2 for i in range(10) if i%2==0])
