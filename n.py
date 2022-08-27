# #Your code goes here
# n = int(input())
# total = 0
# for i in range(1, n+1):
#     if (i%2) ==0:
#         total =total + i

# print(total)

num = int(input())
sum = []
s = []
for i in range(1,num+1):
    if (i%2)==0:
        print(i)
    for j in range(1,num+1):
        if (j%3)==0:
            print(j)
