"""
Nia Covington
ElementaryStrings.py
Create a program that uses strings and list with techniques of indexing and slicing.
I certify that this assignment is entirely my own work.

"""


def name_reverse():
    name=input("Enter a name (first last):")
    first_name, last_name = name.split(" ")
    print(f"{last_name},{first_name}")

def company_name():
    domain=input("enter a domain:")
    www,companyname,com= domain.split(".")
    print(companyname)

def initials():
    num_students=int(input("How many students are in the class?"))
    for i in range(num_students):
        student_name=input("What is the name of student?")
        first_name,last_name = student_name.split(" ")
        print(first_name[0]+last_name[0])

def names():
    enter_names=input("Enter a list of names ( separated by commas):")
    list_names= enter_names.split(",")
    for name in list_names:
        split_names=name.split(' ')
        first_initial=str(split_names[-2])
        second_initial= str(split_names[-1])
        print(first_initial[0]+ second_initial[0], end = " ")

def thirds():
    list_sen= []
    all_sent = []
    num_sentences= int(input("Enter a number of sentences:"))
    for i in range(1, num_sentences+1):
        sent= input("Enter sentence" + str(i) +  ":")
        list_sen.append(sent)
    for sent in list_sen:
        new_sentences= ''
        for i in range(0,len(sent),3):
                new_sentences += sent[i]
        all_sent.append(new_sentences)
    for sens in all_sent:
        print(sens)

def word_average():
    sentence= input("Enter a sentence:")
    words=sentence.split()
    average= sum(len(word) for word in words)/len(words)
    print(average)

def pig_latin():
    sentence= input("Enter a sentence to convert to pig latin:")
    words= sentence.split(" ")
    for word in words:
        moved_letter = word[0]
        word= word.replace(word[0], '')
        print(str(word)+moved_letter, end="ay", sep=" ")


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
