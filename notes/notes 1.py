
def convert():
    # get user input in celsius
    celsius= eval(input("what is the temperature in celsius?"))
    #convert input from celsius to fahrenheit using the equation c * (9/5)+32
    fahrenheit= celsius * 9/5 +32
    #display result to user
    print()
    print("the temperature is", fahrenheit, "degrees fahreneit.", end=" ")
    print('awesome!')

convert()