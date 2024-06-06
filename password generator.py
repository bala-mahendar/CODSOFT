import random as r 

print("  ===========================")
print("||                           ||")
print("||     Password Generator    ||")
print("||                           ||")
print("  ===========================\n")
def leng():
    length = int(input("Enter the length of the password : "))
    return length

def complexi(length):
    chars = []
    chars.extend([chr(r.randint(65, 90)) for _ in range(length // 4)])  # Uppercase letters
    chars.extend([chr(r.randint(97, 122)) for _ in range(length // 4)])  # Lowercase letters
    chars.extend([chr(r.randint(48, 57)) for _ in range(length // 4)])  # Numbers
    chars.extend([chr(r.randint(33, 47) + r.randint(58, 64)) for _ in range(length - (len(chars)))])  # Punctuation and symbols
    r.shuffle(chars)
    t=''.join(chars)
    print(t,"\n\n")

while True:
   complexity = int(input("Enter the complexity of password \n1.Low \n2.Medium \n3.High \n4.Quit \nEnter number for complexity of password : "))
   if complexity in [1,2,3,4]: 
    if complexity == 3:
            print("Length should be greater than 8")
            d = leng()
            if d> 8:
                print(f"The complexity of Password : {d}")
                complexi(d)
            else :
                print(f"Invalid number {d} \nLength of the password must be above 9\n")

    elif complexity==2:
            print("Length should between 4 to 8")
            d = leng()
            if d>3 and d<9:
                print(f"The complexity of Password : {d}\n")
                complexi(d)
            else :
                print(f"Invalid number {d} \nLength of the password should between 4 to 8\n")
    elif complexity==1:
            print("Length will be 4 ")
            print(f"The complexity of Password : 4")
            complexi(4)
    else:
        opt= input("Are you sure wants to quit ?")
        if(opt=='yes'):quit()
        
   else:
    print("Invalid option from complexity { 1,2,3 }\n")
