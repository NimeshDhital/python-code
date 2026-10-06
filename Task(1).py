#Identity operator
a=[1,2,3]
b=[1,2,3]
c=a
print(a is c)
print(a==b)
print(a==c)
print(id(a))
print(id(c))

#assigment operator
print(5 + 3)#addition
print(2 - 1)#Substractiom
print(10/3)#Division
print(10 // 3)# Floor division: 3
print(10 % 3) # Modulus (remainder): 1
print(10 ** 3)# Exponentiation

#comparsion operator
print(1==2)
print(1!=5)
print(1>2)
print(1<2)
print(10>=10)
print(10<=11)

#assignment operator
score = 0
score += 50
score += 10
print(f"{score}")

#logical operator
print(6 and 7)
print(6 or 7)
print(not 6)

# Bitwise Operators

print(5 & 3)    
print(5 | 3)      
print(5 ^ 3)   
print(~5)        
print(5 << 1)      
print(5 >> 1) 

# Membership Operators

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)          
print("orange" in fruits)         
print("orange" not in fruits)     

