#pattern---

# i = 0
# j = 0
# while i <= 5:
#     while j <= 5:
#         print ('*',end = ' ')
#         j += 1
#         print ()
#     i += 1    

# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *



# for i in range(5):
#     for j in range(i):
#         print('*',end = ' ')
#     print()
    
    
    
# * 
# * *
# * * *
# * * * *





# for i in range (1,5):
#     for j in range (1,i+1):
#      print ('*',end = ' ')
#     print()   
    
    
# * 
# * *
# * * *
# * * * *





# for i in range (1,5):
#     for j in range(1,5):
#         print('*',end = ' ')
#     print()
    
    
# * * * * 
# * * * *
# * * * *
# * * * *




# for i in range (1,5):
#     for j in range(1,3):
#         print('*',end = ' ')
#     print()
    
# * * 
# * *
# * *
# * *   


# for i in range (1,6):
#     for j in range(1,3):
#         print(j,end = ' ')
#     print()
    
    
# 1 2 
# 1 2
# 1 2
# 1 2







# for i in range (1,6):
#     for j in range(1,6):
#         print('*',end = ' ')


# * * * * * * * * * * * * * * * * * * * * * * * * * 





# for i in range (1,6):
#     for j in range(0,i):
#         print('*',end = ' ')
#     print()
    
    
    
# * 
# * *
# * * *
# * * * *
# * * * * *






# for i in range (1,6):
#     for j in range(i,6):
#         print('*',end = ' ')
#     print()
    
    
# * * * * * 
# * * * *
# * * *
# * *
# *







# for i in range (1,6):
#     for j in range(i,6):
#         print(i,end = ' ')
#     print()
    
    
# 1 1 1 1 1 
# 2 2 2 2
# 3 3 3
# 4 4
# 5







# a = 1
# for i in range (1,5):
#     for j in range(i):
#         print(a,end = ' ')
#         a += 1
#     print()
    
    
# 1 
# 2 3
# 4 5 6
# 7 8 9 10





# a = 1
# for i in range (1,5):
#     for j in range(i):
#         print(a,end = ' ')
#     print()
    
    
# 1 
# 1 1
# 1 1 1
# 1 1 1 1








# a = 1
# for i in range (1,6):
#     for j in range(i):
#         print(a,end = ' ')
#     a += 1    
#     print()
    
    
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5






# a = 65
# for i in range (1,6):
#     for j in range(i):
#         print(chr(a),end = ' ')
#     a += 1    
#     print()
    
# A 
# B B 
# C C C
# D D D D
# E E E E E







# a = 65
# for i in range (1,6):
#     for j in range(i):
#         print(chr(a),end = ' ') 
#     print()
    
    
# A 
# A A
# A A A
# A A A A
# A A A A A





# a = 65
# for i in range (1,6):
#     for j in range(i):
#         print(chr(a),end = ' ') 
#         a += 1
#     print()


# A 
# B C
# D E F
# G H I J
# K L M N O






# a = 65
# for i in range (1,6):
#     for j in range(1,i+1):
#         print(j,end = ' ') 
#         a += 1
#     print()
    
    
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5








# a = 65
# for i in range (1,6):
#     for j in range(65,i+65):
#         print(j,end = ' ') 
#         a += 1
#     print()
    
    
# 65 
# 65 66
# 65 66 67
# 65 66 67 68
# 65 66 67 68 69









# a = 65
# for i in range (1,6):
#     for j in range(65,i+65):
#         print(chr (j),end = ' ') 
#     print()
    
    
# A 
# A B
# A B C
# A B C D
# A B C D E





# a = 65
# for i in range (1,6):
#     for j in range(a,i+a):
#         print(chr (j),end = ' ') 
#     print()
    

# A 
# A B
# A B C
# A B C D
# A B C D E






# a = 65
# for i in range (5,0,-1):
#     for j in range(a,i+a):     #--(65,i+65),(1,i+1)
#         print(chr (j),end = ' ') 
#     print()
    

# A B C D E 
# A B C D
# A B C
# A B
# A








# a = 65
# for i in range (1,6):
#     for j in range(1,6):
#         print(i,end = ' ') 
#     print()
    
    
# 1 1 1 1 1 
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5








# a = 65
# for i in range (1,6):
#     for j in range(1,6):
#         print(i*j,end = ' ') 
#     print()
    
    
    
# 1 2 3 4 5 
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25







    
    
    
# rows = 5

# for i in range(1, rows + 1):
#     for space in range(rows - i):
#         print(" ", end="")
#     for star in range(i):
#         print("* ", end="")
#     print()
    
    
#     * 
#    * *
#   * * *
#  * * * *
# * * * * *