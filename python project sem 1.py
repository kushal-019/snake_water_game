import game
import notification
# here we imported snake water gun file and notification file to our main file
print("here is a question for you to continue :) ")
print()
a='''question 1
for i in range(10, 15, 1):
    print( i, end=',')'''
print(a)
print()
ans_1=['10', '11', '12', '13', '14']
ans=(input().split(","))
if ans==ans_1:
    notification.noti_1()
    # for correct answer, 1st notification pops up.
    for i in range (3):
        game.swg_game()
else :
    notification.noti_2()
    # for incorrect answer, 2nd notification pops up.
print()
print()

b='''question 2
def calculate (num1, num2=4):
  res = num1 * num2
  print(res)

calculate(5, 6)'''
print(b)
print()
ans_2 = 30
ans=int(input())
if ans==ans_2:

    notification.noti_1()
    for i in range (3):
        game.swg_game()
else :
    notification.noti_2()
print()
print()

c='''question 3
str = "pynative"
print (str[1:3])'''  
print(c)
print()
ans_3 = "yn"
ans=str(input())
if ans==ans_3:
    notification.noti_1()
    for i in range (3):
        game.swg_game()
else :
    notification.noti_2()
print()
print()

d='''question 4
x = 36 / 4 * (3 +  2) * 4 + 2
print(x)'''   
print(d)
print()
ans_4 =182
ans=float(input())
if ans==ans_4:
    notification.noti_1()
    for i in range (3):
        game.swg_game()
else :
    notification.noti_2()
print()
print()

e='''question 5
var = "James" * 2  * 3
print(var)'''
print(e)
print()
ans_5 ="JamesJamesJamesJamesJamesJames"
ans=str(input())
if ans==ans_5:
    notification.noti_1()
    for i in range (3):
        game.swg_game()
else :
    notification.noti_2()
print()
print()
    
print("Game Is Over")


