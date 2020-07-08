# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:32:01 2020

@author: scamp
"""


class Household_Funds():
    def __init__(self,):
        pass
    def __call__(self, household):
        if hasattr(household, 'funds') == False:
            household.funds = 0
            household.__funds = household.funds
        def get_funds(self):
            return self.__funds
        def set_funds(self, newfunds):
            self.__funds += newfunds
        household.get_funds = get_funds
        household.set_funds = set_funds
        newfunds = 0
        for p in household.people:
            newfunds += p.get_money(p)
            p.set_money(p, 0)
        household.set_funds(household, newfunds)
        
hf1 = Household_Funds()