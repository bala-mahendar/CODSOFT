import random as r

print("  =======================================")
print("||                                       ||")
print("||           Rock-Paper-Scissor          ||")
print("||                                       ||")
print("  =======================================")

def rps():
    user_point, comp_point, number = 0, 0, 1
    no_of_times = int(input("\nEnter Number of times want to play the Game : "))
    k = no_of_times
    while  no_of_times>0:
        try:
            print("\nRound : ",number)
            if no_of_times >0:
                print("***************************************")
                print()
                terms = ['Scissor', 'Rock', 'Paper']
                comp = r.choice(terms)
                me = int(input("Choose your option : \n1.Scissor\n2.Rock\n3.Paper\n4.Quit\nEnter number based on option : "))
                if me == 4:  # this condition for quiting the program
                    y_or_no = input("Are you sure want to leave this game (y/n) : ")
                    if y_or_no == 'n' or y_or_no == 'N':
                        continue
                    else:quit()
                if me in range(1,4):
                    me1 = terms[me - 1]
                    if me1 == comp:
                        user_point += 0
                        comp_point += 0
                        print(f'\nComputer == User \n{comp}   {me1} \n NO POINTS')
                    elif me1 != comp:
                        if me1 == 'Rock' and comp == 'Scissor' or me1 == 'Scissor' and comp == 'Paper' or me1 == 'Paper' and comp == 'Rock':
                            print(f'\nComputer < User \n{comp}   {me1}')
                            user_point += 1
                        else:
                            print(f'\nComputer > User \n{comp}   {me1}')
                            comp_point += 1
                else:
                    print("Invalid !!!")
                    continue
                no_of_times -= 1
                number += 1
        except ValueError as e:
            print("Please enter the correct value !")

    print("\n=====================\nResult : ")
    if user_point >= (k/2):
        print(f"User wins => POINTS : {user_point} ")
    elif user_point == comp_point:
        print(f'====== TEI ======\nUser : {user_point}\nComputer : {comp_point}')
    elif comp_point >=(k/2):
        print(f"Computer wins => POINTS : {comp_point}")
    print("======================")

rps()
while True :
    try:
        play_again = input("\n****************************************\nDo you want to play again (y/n) ? : ").lower()
        if play_again == 'n':
            quit()
        else:rps()
    except ValueError :
        print("Invalid !!!")