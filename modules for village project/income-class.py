# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:08:05 2020

@author: scamp
"""


from numpy.random import choice
jobs = []
jobprobs = []
jobs_rates_pay = {'blacksmith':(.2,50),'farmer':(.5,20),'governor':(.01,1000),
               'Landlord':(.05,200),'builder':(.2,50),'merchant':(.04,250),'weaver':(0,5),
               'child':(0,2),'infant':(0,0),'elderly':(0,0)}
for job in jobs_rates_pay:
    jobs.append(job)
    jobprobs.append(jobs_rates_pay[job][0])

class Income():
    def __init__(self, jobs = jobs, jobprobs = jobprobs,
                 jobs_rates_pay = jobs_rates_pay):
        self.jobs = jobs
        self.jobprobs = jobprobs
        self.jobs_rates_pay = jobs_rates_pay
        
    def __call__(self, villager):
        if hasattr(villager, 'money') == False:
            villager.money = 0
            villager.__money = villager.money
            def get_money(self):
                return self.__money
            def set_money(self, income):
                self.__money += income
            villager.get_money = get_money
            villager.set_money = set_money
        #for now, income comes only from jobs but I want it to include
        #inheritance
        income = jobs_rates_pay[villager.get_profession(villager)][1]
        villager.set_money(villager, income)

income1 = Income()