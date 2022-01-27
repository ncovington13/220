"""
Nia Covington
lab2.py
Calculating Mean
Create a program that will take a certain number of values, accept inputs, and output three different methods of
computing the mean (root mean square, harmonic mean, geometric mean).
I certify that this is my own work.
"""


def means():
    mean_value= int(input("Enter the values to be entered?"))
    # represents the value "n" in equation
    root_mean_square_acc=0.0
    harmonic_mean_acc=0.0
    geometric_mean_acc=1
    # represents the accumulators different ways that the mean will be calculated
    for i in range(mean_value):
        value_number= float(input("Enter value:"))
        # this represents the value "x" in the equation
        root_mean_square_acc= root_mean_square_acc + (value_number**2)
        harmonic_mean_acc= harmonic_mean_acc + (1/value_number)
        geometric_mean_acc= geometric_mean_acc * value_number
    rms=(root_mean_square_acc/mean_value)**(1/2)
    # equation for root mean square method
    harmonic_mean= (mean_value/harmonic_mean_acc)
    # equation for harmonic mean method
    geometric_mean= geometric_mean_acc**(1/mean_value)
    # equation for geometric mean
    print("The value of the root mean square=", rms)
    print("The value of the harmonic mean=", harmonic_mean)
    print("The value of the geometric mean=", geometric_mean)
means()