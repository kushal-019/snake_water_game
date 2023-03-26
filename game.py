from random import choice
def swg_game():
    li=["s","w","g"]
    print()
    me=str(input("choose from s,w,g : " ).lower())
    comp=choice(li)
    # it allows computor to automatically choose any char from list
    print("comp chose:",comp)
    print()
    if me=="s" and comp=="w":
        print("you wins")    
    elif me=="s" and comp=="g":
        print('comp wins')   
    