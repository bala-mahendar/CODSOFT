import pickle as p
def banner():
    print("  =========================")
    print("||                         ||")
    print("||       CONTACT-BOOK      ||")
    print("||                         ||")
    print("  =========================\n")

def scrible(contacts):
    with open("data.dat","wb") as f:
        p.dump(contacts,f)

def loading():
    try:
        with open("data.dat","rb") as f1:
            return p.load(f1)
    except FileNotFoundError:
        print("No contact data found. Starting with an empty database.")
        return {}
    except:
        return "Nothing Buddy"

contact_book = loading()
def add():
        task = int(input("\n======================\nEnter Number of contacts to Add : "))
        for i in range(task):
                print(f"\nContact {i+1}")
                name = input("Enter the name : ")
                while True:
                    try:
                        ph = int(input("Enter the phone : "))
                        break
                    except ValueError:
                        print("Invalid !!!")
                email = input("Enter the Email  : ")
                contact = {"Phone Number : ": ph,\
                           "Email        : ":email}
                contact_book[name] = contact
        scrible(contact_book)
        view()
    
    
    
def remove():
    task = int(input("\n======================\nEnter Number of contacts to Delete : "))
    for _ in range(task):
        contact_name = input("Enter the Contact name : ")
        if contact_name in contact_book:
            del contact_book[contact_name]
        else:
            print("There is no Contact based on your search !!!")
    print("After Deleting :\n")
    scrible(contact_book)
    view()

def view():
    print("\nContact : ")
    k=1
    if not contact_book:
        print("There is no Contact !!!\n")
    else:
        for i in contact_book:
            print(f"\nName         :  {i}")
            for key, val in contact_book[i].items():
                print(f"{key} {val}")
            k+=1

def search():
    while True:
        try:
            task = int(input("\n======================\nEnter Number of contacts to Search : "))
            break
        except:print("Invalid !!!\n")
    for _ in range(task):
        contact_name = input("Enter the Contact name : ")
        if contact_name in contact_book:
            for i,j in contact_book[contact_name].items():
                print(f"{i} {j}")
        else:
            print("There is no Contact based on your search !!!")

def main():
    banner()
    while True:
      options = int(input("\nWelcome to Contact Book\n=======================\
                          \n1.Add contact\n2.View contact\n3.Search contact\
                          \n4.Update contact\n5.Delete\n6.Quit\nEnter the option : "))
      if options in range(1,7):
            if options==1:add()
            elif options==2:view()
            elif options==3:search()
            elif options==4:add()
            elif options==5:remove()
            elif options==6:
                y_or_no = input("Are you sure want to quit? (y/n): ").lower()
                if y_or_no=='y':
                    scrible(contact_book)
                    quit()
                else: continue
      else:
         print("Invalid Option !!!")

if __name__ == '__main__' :
    main()