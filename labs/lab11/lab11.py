"""
Nia Covington
lab11.py
Create a program that plays a three door game.
I certify this is my own work.
"""

from lab10.door import Door
from lab10.button import Button
from random import randint
from graphics import *

def three_door_game():
    win=GraphWin("Three Door Game", 500,500)
    door1=Door(Rectangle(Point(75,200),Point(175,450)),"Door 1")
    door1.color_door('grey')
    door1.draw(win)
    door2=Door(Rectangle(Point(200,200),Point(300,450)),"Door 2")
    door2.color_door('grey')
    door2.draw(win)
    door3=Door(Rectangle(Point(325,200),Point(425,450)), "Door 3")
    door3.color_door('grey')
    door3.draw(win)
    win.setBackground('light blue')
    button=Button(Rectangle(Point(400,50),Point(450,125)),"Quit")
    button.draw(win)
    scoreboardR=Rectangle(Point(50,50),Point(125,125))
    scoreboardL=Rectangle(Point(125,50),Point(200,125))
    scoreboardR.draw(win)
    scoreboardL.draw(win)
    instructions=Text(Point(250,150),"I have a secret door!")
    instructions.draw(win)
    wins=Text(Point(90,45),"wins")
    loss=Text(Point(150,45),"losses")
    wins.draw(win)
    loss.draw(win)
    loss_count=0
    loss_count_text=Text(scoreboardL.getCenter(), str(loss_count))
    loss_count_text.draw(win)
    win_count=0
    win_count_text=Text(scoreboardR.getCenter(),str(win_count))
    win_count_text.draw(win)
    message=Text(Point(235,475),"Click to guess where the secret door is")
    message.draw(win)
    # draws the format of the game

    doors=[door1,door2,door3]
    doors[randint(0,len(doors)-1)].set_secret(True)
    click=win.getMouse()
    while not button.is_clicked(click):
        for door in doors:
            if door.is_clicked(click):
                if door.is_secret():
                    door.color_door('green')
                    win_count+=1
                    win_count_text.setText(str(win_count))
                    instructions.setText('you win!')
                    message.undraw()
                else:
                    message.undraw()
                    door.color_door('red')
                    loss_count+=1
                    loss_count_text.setText(str(loss_count))
                    if door1.is_secret():
                        door1.color_door('green')
                    elif door2.is_secret():
                        door2.color_door('green')
                    elif door3.is_secret():
                        door3.color_door('green')
                    instructions.setText('sorry incorrect!')
        restart=Text(Point(235,475),"Click anywhere to play again!")
        restart.draw(win)
        click = win.getMouse()
        if button.is_clicked(click):
            break
        for door in doors:
            door.color_door('grey')
            door.set_secret(False)
        doors[randint(0, len(doors) - 1)].set_secret(True)
        restart.undraw()
        message.setText("Click to guess where the secret door is")
        instructions.setText("I have a secret door!")
        click = win.getMouse()
    win.close()
