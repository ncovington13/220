"""
Nia Covington
salesperson.py
Create a class that encapsulates data for a sales person
I certify this is my own work.
"""

class Sales_person:
    def __init__(self,employee_id,name):
        self.employee_id=employee_id
        self.name=name
        self.sales=[]

    def get_id(self):
        employee_id=self.employee_id
        return int(employee_id)
    def get_name(self):
        name=self.name
        return str(name)
    def set_name(self,name):
        self.name=name
    def enter_sale(self,sale):
       self.sales.append(sale)
    def total_sales(self):
        return sum(self.sales)
    def get_sales(self):
        return self.sales
    def met_quota(self,quota):
        if (self.total_sales() >= quota):
            return True
        return False
    def compare_to(self,other):
        if (other.total_sales() == self.total_sales()):
            return 0
        elif (other.total_sales() < self.total_sales()):
            return 1
        else:
            return -1
    def __str__(self):
        string= str(self.employee_id)+ "-" +self.name + ":" + str(self.total_sales())
        return string

