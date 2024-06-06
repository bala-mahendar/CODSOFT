# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.

# Perform the calculation and display the result.

print("  =========================")
print("||                         ||")
print("||        CALCULATOR       ||")
print("||                         ||")
print("  =========================\n")

def calculation(n1, n2, op):
    try :
        if op == '+':  print("\nAnswer = ",n1+n2,"\n")
        elif op == '-':print("\nAnswer = ",n1-n2,"\n")
        elif op == '/':print("\nAnswer = ",n1/n2,"\n")
        elif op == '*':print("\nAnswer = ",n1*n2,"\n")
    except ZeroDivisionError : print("\nInvalid operation so dont try to do --- VALUE/0 ---")

while  True :
    try :
      num1 = int(input("Enter the numnber 1 :"))
      num2 = int(input("Enter the numnber 2 :"))
      operator = input("Enter operator { +, -, *, / } : ")
      if operator in ['-','*','+','/']:  
        calculation(num1, num2, operator)    
        yorn = input("\nAre you like to continue ? (y/n) : ")
        if yorn == 'n': break
      else: 
        print("Invalid operator ! ")
    except ValueError:
       print("Pls check the values ! So start it first \n")

          