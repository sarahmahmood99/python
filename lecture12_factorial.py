#n! = n *(n-1) * (n-2) *  . . . . * 1 
#6! = 6*5*4*3*2*1 = 720

fact=1
for i in [6,5,4,3,2,1]:
  fact=fact * i

print("the factorial: ", fact )

#//////////another //////
fact=1
for i in [2,3,4,5,6]:
  fact=fact * i

print("the factorial: ", fact )


#////for big numbers /////////
x=(list(range(10)))   #from 0 to 9 
print(x)

x=(list(range(1,10)))   #from 1 to 9 
print(x)

x=(list(range(4,10)))   #from 4 to 9 
print(x)

x=(list(range(1,10,2)))   #from 1 to 9  but 2 steps
print(x)

print()
print()
print()

# /////// use range in function fact ///////

def main():
  number=int(input("enter a number , please: "))
  fact=1
  for i in range(number,1,-1):
    fact=fact * i
  print("the factorial of ", number , "is ", fact)
main()

#//////////another //////

def factorial():
  number=int(input("enter a number , please: "))
  fact=1
  for i in range(1,number+1,1):
    fact=fact * i
  print("the factorial of ", number , "is ", fact)
factorial() 
