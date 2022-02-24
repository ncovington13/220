"""
Nia Covington
lab6.py
Vignere
Create a program that processes string data while using graphics.
I certify that this is my own work.
"""

from graphics import *
from math import *

def vignere(keyword=None):
    win=GraphWin("Vigenere",500,500)
    open_box=Rectangle(Point(50,50),Point(450,450))
    open_box.setFill('gray')
    open_box.draw(win)

    message_code=Text(Point(125,200),"Message to Code")
    message_code.setTextColor('black')
    message_code.draw(win)

    entry_box=Entry(Point(285,200),30)
    entry_box.setFill('dark grey')
    entry_box.setTextColor('black')
    entry_box.draw(win)

    keyword_code=Text(Point(125,250),"Enter Keyword")
    keyword_code.setTextColor('black')
    keyword_code.draw(win)

    keyword_box=Entry(Point(225,250),13)
    keyword_box.setFill('dark grey')
    keyword_box.setTextColor('black')
    keyword_box.draw(win)

    encode_box=Rectangle(Point(175,300), Point(275,350))
    encode_box.setOutline('black')
    encode_box.draw(win)
    encode_message=Text(Point(225,325),"Encode")
    encode_message.setTextColor('black')
    encode_message.setSize(18)
    encode_message.draw(win)
    win.getMouse()
    encode_message.undraw()
    encode_box.undraw()

    message=entry_box.getText()
    message=message.upper()
    message=message.replace(" ","")
    keyword=keyword_box.getText()
    keyword=keyword.upper()
    keyword=keyword.replace(" ","")

    # message[i]
    # key[i]
    strings=""
    for i in range(len(message)):
        coord=ord(message[i])-65
        other_cord=ord(keyword[i % len(keyword)])-65
        shift_code= coord+other_cord
        shift_code= shift_code % 26
        final_code=chr(shift_code+65)
        strings=strings+final_code

    result_message=Text(Point(225,325),"Resulting Message:")
    answer=Text(Point(225,350),strings)
    result_message.draw(win)
    answer.draw(win)


    close_instruct=Text(Point(225,425),"Click Anywhere to Close!")
    close_instruct.setSize(16)
    close_instruct.draw(win)
    win.getMouse()
    win.close()
