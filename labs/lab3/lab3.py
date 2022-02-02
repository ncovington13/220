"""
Nia Covington
Traffic Patterns
Create a program that will analyze traffic patterns based off user input.
I certify this is my own work.
"""

def traffic():
    total_roads= eval(input("How many roads were surveyed?"))
    total_average_acc= 0
    # accumulator for the total average of vehicles per road
    for i in range(1,total_roads+1):
        # asks questions without repeatedly inputing same information
        print("How many days was road", i, "surveyed?")
        days_surveyed= eval(input(""))
        car_average_acc = 0
        # accumulator for solving car average
        for j in range(1,days_surveyed+1):
            print("How many cars traveled on day",j,"?")
            cars_traveled= eval(input(""))
            car_average_acc= car_average_acc+ cars_traveled
        average_vehicles=car_average_acc/days_surveyed
        # equation used to solve for average vehicles in a day
        total_average_acc= total_average_acc+car_average_acc
        print("Road",i,"vehicles per day ?", average_vehicles)

    print("Total number of vehicles:",total_average_acc)
    average_per_road= total_average_acc/ total_roads
    print("Average number of vehicles per road:", average_per_road)

traffic()
