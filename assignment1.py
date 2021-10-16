'''
Write a program to calculate the volume and surface area of 
a sphere from its radius, given as input. Here are some 
formulas that might be useful:
اكتب برنامجًا لحساب حجم ومساحة سطح الكرة من نصف قطرها
 ، كمدخلات.  فيما يلي بعض الصيغ التي قد تكون مفيدة:
'''


#sarah mahmood 
#assignment1

import math

def calculate(): 
  rad=eval(input("enter the redius of sphere, please: "))
  print()

  volume=4/3*math.pi*(rad**3)
  print("the volume of a sphere is : ",volume)
  
  surface=math.pi*(rad**2)
  print("the surface of a sphere is :",surface)
calculate()
