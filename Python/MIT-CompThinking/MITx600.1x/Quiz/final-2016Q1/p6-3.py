#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        # print('Person:')
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        # print('Person-name:')
        return self.name

class Lecturer(Person):     
    def lecture(self, stuff):         
        # print('Lecture:')
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer):
    def __init__(self, name):
        self.name = 'Prof. ' + name
        self.localname = name

    def lecture(self, stuff):
        return 'I believe that ' + self.localname + ' says: ' + stuff

    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def lecture(self, stuff):
        # print('ArrogantProfessor:')
        return 'It is obvious that ' + Professor.lecture(self, stuff)

    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)



if __name__ == '__main__':
    e = Person('eric') 
    le = Lecturer('eric') 
    pe = Professor('eric') 
    ae = ArrogantProfessor('eric')


    print(e.say('the sky is blue'))
    print(le.say('the sky is blue'))
    print(le.lecture('the sky is blue'))
    print(pe.say('the sky is blue'))        #
    print(pe.lecture('the sky is blue'))
    print(ae.say('the sky is blue'))        #
    print(ae.lecture('the sky is blue'))


'''
>>> e.say('the sky is blue')
eric says: the sky is blue

>>> le.say('the sky is blue')
eric says: the sky is blue

>>> le.lecture('the sky is blue')
I believe that eric says: the sky is blue

>>> pe.say('the sky is blue')
Prof. eric says: I believe that eric says: the sky is blue 

>>> pe.lecture('the sky is blue')
I believe that eric says: the sky is blue

>>> ae.say('the sky is blue')
Prof. eric says: It is obvious that I believe that eric says: the sky is blue 

>>> ae.lecture('the sky is blue')
It is obvious that I believe that eric says: the sky is blue
'''


    

