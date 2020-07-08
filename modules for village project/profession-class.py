# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:39:55 2020

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
class Profession():
    
    def __init__(self,infancy = 7, adolescence = 14, oldage = 65, jobs = jobs,
                 jobprobs = jobprobs, jobs_rates_pay = jobs_rates_pay):
        self.infancy = infancy
        self.adolescence = adolescence
        self.oldage = oldage
        self.jobs = jobs
        self.jobprobs = jobprobs
        self.jobs_rates_pay = jobs_rates_pay
        
    def __call__(self, villager):
        if hasattr(villager, 'profession') == False:
            villager.profession = None
            villager.__profession = villager.profession
            def get_profession(self):
                return self.__profession
            def set_profession(self, newprofession):
                self.__profession = newprofession
            villager.get_profession = get_profession
            villager.set_profession = set_profession

        profession = villager.get_profession(villager)
        age = villager.age
        
        if villager.sex == male:
            if age <= self.infancy:
                profession = 'infant'
            elif age <= self.adolescence:
                profession = 'child'
            elif age <= self.oldage:
                    if profession is None or 'child':
                        if profession not in jobs or profession == 'child':
                            profession = choice(self.jobs,p=self.jobprobs)
            else:
                profession = 'elderly'
        if villager.sex == female:
            if age <= self.infancy:
                profession = 'infant'
            elif age <= self.adolescence:
                profession = 'child'
            elif age <= self.oldage:
                    if profession is None or 'child':
                        if profession not in jobs or profession == 'child':
                            profession = 'weaver'
            else:
                profession = 'elderly'
        villager.set_profession(villager,profession)

        


pd1 = Profession()
