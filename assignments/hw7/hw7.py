"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

import math
def number_words(in_file_name: str, out_file_name: str):
    count=0
    input=open(in_file_name,"r")
    output = open(out_file_name, "w")
    lines=input.readlines()
    for line in lines:
        words=line.split(" ")
        for word in words:
            count+=1
    output.write('str(count)' + " "+ format.(word))


def hourly_wages(in_file_name:str, out_file_name:str):
    input=open(in_file_name,"r")
    output=open(out_file_name,"w")
    lines=input.readlines()
    for line in lines:
        attributes=line.split(" ")
        attributes[2]= float(attributes[2] + 1.65)
        result="{}{} {:.2f}".format(attributes[0],attributes[1],attributes[2]* float(attributes[3]))
    output.write(result)


def calc_check_sum(isbn:str)->int:
    newISBN=isbn.replace("-","")
    if len(newISBN)!=10:
        print("Invalid ISBN number. Needs to be 10 digits!")
        exit(0)
    isbn_number=int(newISBN)
    check_sum_result=0
    index=1
    while(isbn_number !=0):
        check_sum_result+=(isbn_number%10)* index
        math.floor(isbn_number/10)
        index+=1
    return check_sum_result

def send_message(file_name, friend_name):
    infile= open(file_name,"r")
    fileName="{}.txt".format(friend_name)
    outfile=open(fileName,"w")
    lines=infile.readlines()
    for line in lines:
        print(str(line), end="", file=outfile)
    infile.close()
    outfile.close()
def encode(user_input,user_input2):
    answer="".join(chr(ord(c)+ int(user_input2)) for c in user_input)
    return answer


def send_safe_message(file_name, friend_name, key):
    infile=open(file_name,"r")
    fileName="{}.txt".format(friend_name)
    outfile= open (fileName,"w")
    lines=infile.readlines()
    for line in lines:
        ans=encode(str(line),key)
        outfile.write(ans, end="")
    infile.close()
    outfile.close()

def send_uncrackable_message(file_name, friend_name, pad_file_name):
    infile=open(file_name,"r")
    infile.readlines()

if __name__ == '__main__':
    pass
