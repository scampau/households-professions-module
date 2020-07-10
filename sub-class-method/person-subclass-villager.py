# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:27:46 2020

@author: scamp
"""


from numpy.random import choice

jobs_rates_pay = {'blacksmith':(.2,50),'farmer':(.5,20),'governor':(.01,1000),
               'Landlord':(.05,200),'builder':(.2,50),'merchant':(.04,250),'weaver':(0,5),
               'adolescent':(0,2),'child':(0,0),'elderly':(0,0)}
childhood = 7
adolescence = 14
oldage = 65

class Villager(Person):

    def __init__(self, sex, age, has_community, has_house, marriagerule, inheritancerule,
                 mobilityrule, birthrule, mother = None, father = None,
                 profession = None):
        super().__init__(sex, age, has_community, has_house, marriagerule, inheritancerule, 
                         mobilityrule, birthrule, mother, father)
        jobs = []
        jobprobs = []
        self.jobs_rates_pay = jobs_rates_pay
        for job in jobs_rates_pay:
            jobs.append(job)
            jobprobs.append(jobs_rates_pay[job][0])
        self.jobs = jobs
        self.jobprobs = jobprobs
        self.profession = profession
        self.money = 0
        self.father = father
        self.mother = mother
        self.childhood = childhood
        self.adolescence = adolescence
        self.oldage = oldage
        
    
    def pro_dev(self):

        
        if self.age <= childhood:
            self.profession = 'child'

        elif self.age <= adolescence:
            self.professon = 'adolescent'

        elif self.age <= oldage:
            if self.sex == male:
                if self.father == None:
                    if self.profession is None or self.profession is 'child':
                            self.profession = choice(self.jobs,p=self.jobprobs)
                else:
                    self.profession = self.father.profession
                    if self.father.profession == 'governor' or self.father.profession == 'Landlord':
                        if self.father.lifestatus != dead:
                            self.profession = None
            
            if self.sex == female:
                if self.mother == None:
                    if self.profession is None or self.profession is 'child':
                            self.profession = 'weaver'
                else:
                    self.profession = self.mother.profession
        else:
            self.profession = 'elderly'
            
    def income(self):
        if self.profession == None:
            pass
        else:
            self.money += self.jobs_rates_pay[self.profession][1]
        