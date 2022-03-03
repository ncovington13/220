"""
Nia Covington
lab7.py
Weighted Average
Develop a Python program that uses numeric data from a text file
I certify this is my own work.
"""

def weighted_average(input_file,output_file):
    out_file=open(output_file, "w")
    class_avg=0
    valid_std=0
    with open(input_file) as fp:
        content=fp.readlines()
    for line in content:
        line_info= line.split(":")
        numbers= line_info[1].strip().split(" ")
        count=0
        grade_avg=0
        weight_acc=0
        for i in range(len(numbers)//2):
            weight = numbers[count]
            grade= numbers[count + 1]
            count= count + 2
            # indicates where the number is going to start
            grade_avg= (eval(weight) * eval(grade))+grade_avg
            weight_acc=weight_acc + eval(weight)
        grade_avg=grade_avg/100
        if weight_acc > 100:
            print("Oh no! The weights are greater than 100.")
        if weight_acc < 100:
            print("Oh no! The weights are less than 100.")
        if weight_acc == 100:
            print(grade_avg)
            valid_std=valid_std+ 1
            # represents the valid students that would be at end of calculation
            class_avg=class_avg + grade_avg
        out_file.write(line_info[0]+"'s average:")
        out_file.write("{:.1f}".format(grade_avg)+"\n")
    class_avg=class_avg/valid_std
    out_file.write('Class average: {:.1f}'.format(class_avg))

weighted_average("grades.txt","output_file.txt")


