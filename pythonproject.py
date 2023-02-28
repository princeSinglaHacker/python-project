print("Hello, welcome to this game you will find 4 option and you will select one option")
print('1. Addition')
print('2. Square')
print('3. Multiplication')
print('4. Game')
print("You have four option and what do you want 'Please enter number'")
print("If you want to play game so I give fifth option so enjoy game with popcorn")
numbers=int(input("Which number do you want"))
if(numbers==1):
    print("Hello, You choose addition to add numbers")
    size=int(input("what is your size to add number"))
    count=0
    for i in range(size):
        number=int(input())
        count=count+number
    print("Ans is:- "+count)

elif numbers==2:
    print("Hello, You choose square to squaring numbers")
    square=int(input("Enter your number which you want to do square"))
    ans=square*square
    print("Ans is:- "+ans)

elif numbers==3:
    print("Hello, You choose multiplication to multiply numbers")
    size=int(input("what is your size to multiply number"))
    count=1
    for i in range(size):
        number=int(input())
        count=count*number
    print("Ans is:- "+count)

else:
    print("You have 3 option what do you choose")
    name1=input("Enter first player name")
    name2=input("Enter second player name")
    my_turn=input("First player choose- Rock(r),sessior(s),paper(p)")
    dost_turn=input("Second player choose- Rock(r),sessior(s),paper(p)")
    if my_turn=='r':
        if(dost_turn=='s'):
            print("winner is:- "+name1)
        elif(dost_turn=='p'):
            print("winner is:- "+name2)
        else:
            print("This game is tie")

    elif(my_turn=='s'):
        if(dost_turn=='p'):
            print("winner is:- "+name1)
        elif(dost_turn=='r'):
            print("winner is:- "+name2)
        else:
            print("This game is tie")

    elif (my_turn=='p'):
        if(dost_turn=='r'):
            print("winner is:- "+name1)
        elif(dost_turn=='s'):
            print("winner is:- "+name2)
        else:
            print("This game is tie")
    else:
        print("Invalid Syntax")




