print("  =========================")
print("||                         ||")
print("||        TO-DO-LIST       ||")
print("||                         ||")
print("  =========================\n")
def add():
    print("\n==========================\n CREATING / APPENDING \n==========================")
    try:
        print("\n=======================================")
        ran = int(input("Enter number of task : "))
        for _ in range(ran):
            with open("database.txt",'a') as f:
                task = input("Task    : ")
                f.write(task+"\n")
        view()
    except ValueError as e:
        print("Invalid ! So pls Enter Numeric Value !")

def remove():
    print("\n==========================\n REMOVING \n===========================")
    try:
        view()
        print("==========================================\n")
        id = int(input("Enter the TASK Number (digits only): "))
        with open("database.txt",'r') as f:
            todo = f.readlines()
        for i ,t in enumerate(todo):
            if i+1 == id:
                del todo[i]
                break
        with open('database.txt','w') as f:
            f.writelines(todo)
        view()
    except ValueError as e:
        print(e)
        
def view():
    print("\n========== TASK ==========")
    with open("database.txt", 'r') as f:
        tasks = f.readlines()
        count = 1 
        for task in tasks:
            print(f"{count}. {task.strip()}")  
            count += 1

def clearall():
    with open("database.txt",'w') as f:
        f.write("")
    view()

def main():
    while(True):
        try:
            print("\n========================================================\nEnter operations:\n")
            operation = int(input("1.Create\n2.Remove\n3.Update\n4.View\n5.Clear-All\n6.Quit\nEnter the option : "))
            if operation in range(1, 7):        
                if operation==1 or operation==3:   
                    add()
                elif operation==2: 
                    remove()
                elif operation==4: 
                    view()
                elif operation==5:
                    g = input("Are you sure want to clear all  (y/n) ? :")
                    if g=='y':
                        clearall()
                else:
                    opt= input("Are you sure wants to quit ? (y/n)")
                    if(opt=='y' or opt=='Y'):
                        quit()
            else:
                print("Invalid operation ! ")
        except ValueError as e:
            print("Invalid ! So pls Enter Numeric Value !")

if __name__ == "__main__" :
    main()

