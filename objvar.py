class Person:
    "Represent aperson."
    population=0

    def __init__(self,name):
        "Initializes the person's data."
        self.name=name
        print("Initializing%s"%self.name)
        Person.population+=1
    def __del__(self):
        "I'm dying"
        print ("%s says bye."%self.name)
        Person.population-=1
        if Person.population==0:
            
            print('I am the last one.')
        else:
            print('there are still %d person left.'%Person.populatin)
    def sayHi(self):
        print('Hi,my name is %s'%self.name) 
    def howMany(self):
        if Person.population==1:
            print('I am the only person here.')
        else:
            print("we have %d persons here."%Person.population)
swaroop=Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam=Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()
    
 
