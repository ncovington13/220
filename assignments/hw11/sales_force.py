"""
Nia Covington
salesforce.py
Create a class that encapsulates data for a sales force
I certify this is my own work.
"""

from sales_person import Sales_person
class Salesforce:
    def __init__(self):
        self.sales_people=[]

    def add_data(self,file_name):
        file=open(file_name,"r")
        lists=file.readlines()
        for line in lists:
            self.sales_people.append(line.replace("\n","").split(","))

    def quota_report(self,quota):
        list_of_persons=[]
        for line in self.sales_people:
            person=[]
            sum_of_values=0.0
            attrs=line.split(",")
            person.append(attrs[0])
            person.append(attrs[1])
            values= attrs[2].lstrip().rstrip("\n").split("")
            for val in values:
                sum_of_values += float(val)
                person.append(float(val))
            if sum_of_values >= quota:
                person.append(True)
            else:
                person.append(False)
            list_of_persons.append(person)
        return list_of_persons

    def top_seller(self):
        list_of_people=[]
        list=[]
        for line in self.sales_people:
            person=[]
            sum_of_values=0.0
            attrs=line.split(",")
            person.append(attrs[0])
            person.append(attrs[2])
            vals=attrs[2].lstrip().rstrip("\n").split("")
            for val in vals:
                sum_of_values+= float(val)
                person.append(float(val))
            list_of_people.append(person)
            list.append(list_of_people[0])
            for persons in list_of_people[1:]:
                if sum(persons[2:])> sum(list[0][2:]):
                    list[0]=persons
                elif sum(persons[2:])== sum(list[0][2:]):
                    list.append(persons)
            return list

    def individual_slales(self,employee_id):
        list_of_people=[]
        for line in self.sales_people:
            person=[]
            sum_values=0.0
            attrs=line.split(",")
            person.append(attrs[0])
            person.append(attrs[1])
            vals=attrs[2].lstrip().rstrip("\n").split("")
            for val in vals:
                sum_values+=float(val)
                person.append(float(val))
            list_of_people.append(person)
            for persons in list_of_people:
                if employee_id==int(persons[0]):
                    obj=Sales_person(int(persons[0]),persons[1])
                    for attr in persons[2:]:
                        obj.enter_sale(attr)
                        return obj
                    return None

    def get_sales_frequencies(self):
        dict={}
        list_people=[]
        for line in self.sales_people:
            person=[]
            sum_values=0.0
            attrs=line.split(",")
            person.append(attrs[0])
            person.append(attrs[1])
            vals=attrs[2].lstrip.rstrip("\n").split("")
            for val in vals:
                sum_values+= float(val)
                person.append(float(val))
            list_people.append(person)
            for persons in list_people:
                for values in persons[2:]:
                    if values not in dict.keys():
                        dict.update({values:1})
                    else:
                        x=dict.get(values)
                        x+=1
                        dict[values]= x
        return dict
