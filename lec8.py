x=5
print(x)

x=7
print(x)     #the last var of x is print
#/////////////////////////////////

#<var> = input (<prampt>)
name= input("enter your name , please") 
print("hi ", name)

number=eval( input("enter your number , please") )
print(number + 1 )

#////////////////////////////////////////
x=3
y=4
sum=x+y
dif=y-x
print(sum , dif )
 
 #////////////////the same thing but pro ////
x=3
y=4
sum ,dif =x+y , y-x
print(sum , dif )

sum ,dif , mul =x+y , y-x , x*y
print(sum , dif , mul )

#/////////////////////////////////
#swiping 
#x=5 ,y=8 
x,y = 5 , 8 
print(x,y) 
print()

temp=x
x=y
y=temp 
print(x,y) 
print()
#////////////////the same thing but pro ////
x,y = 7 , 3 
print(x,y)  
print()

x,y = y ,x 
print(x,y) 
print()

#///////////////////////////////////////
def main():
  score1 , score2 = eval(input("enter the scores , please"))
  avg=(score1+score2)/2
  print(avg)

main()

