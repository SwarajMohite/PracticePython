# Made by Swaraj
# Date : 8th June 2024
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
choice=int(input("1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n 5 for exponent\n Enter Choice: "))
if(choice==1):
  print(num1,"+",num2,"=",num1+num2)
if(choice==2):
  print(num1,"-",num2,"=",num1-num2)
if(choice==3):
  print(num1,"*",num2,"=",num1*num2)
if(choice==4):
  print(num1,"/",num2,"=",num1/num2)
  print(num1,"%",num2,"=",num1%num2)
if(choice==5):
  print(num1,"^",num2,"=",num1**num2)
else :
  print("\nInvalid Choice")
