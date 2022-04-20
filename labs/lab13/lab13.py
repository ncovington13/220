"""
Nia Covington
lab13.py
Solve a real world problem with all knowledge and skills.
I certify this is my own work
"""
from lab12 import algorithms
def trade_alert(filename):
    in_file=open(filename,"r")
    rfile=in_file.readline()
    acc=0
    numb=rfile.split(" ")
    for i in numb:
        time=acc+1
        acc=acc+1
        if int(i) > 830:
            print("Warning! There is over 830 trades.")
            print("Warning happened at",time)
        elif int(i) == 500:
            print("Pay attention! Trading volume is exactly 500.")
            print("Message happened at", time)
    in_file.close()



