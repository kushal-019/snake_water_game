from plyer import notification
def noti_1():
    notification.notify(
        title = "you gave a correct answer",
        #content appears as highlight
        message = "you won a chance to play a game",
        # text appears in small font 
    )
def noti_2():
    notification.notify(
        title = "you gave a wrong answer",
        message = "you lost a chance to play a game",     
    )
