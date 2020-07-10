# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 16:01:59 2020

@author: scamp
"""


class Commune(House):
    
    def __init__(self,maxpeople,has_community):
        super().__init__(maxpeople,has_community)
        self.money = 0
        self.expenses = 0
    
    def household_income(self):
        for p in self.people:
            self.money += p.money
            p.money = 0
    
    def household_expenses(self):
        for p in self.people:
            if p.sex == male and p.age in range(p.adolescence,p.oldage):
                if p.profession != None:
                    self.expenses += (p.jobs_rates_pay[p.profession][1])*0.1
                else:
                    self.expenses += 5
            self.expenses += 2
        
        self.money -= self.expenses