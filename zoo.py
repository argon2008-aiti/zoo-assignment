class Zoo:


    def __init__(self,name,location,date):
    self.name = name
    self.location = location
	


class Structure(Zoo)
    def __init__(self,name,location,section,date,accomodation):

        Zoo.__init__(self,name,date,location)

        
        

    
class Human(Zoo):

    def __init__(self,name,date,location,age,status,ID,gender):


        Zoo.__init__(self,name,date,location)


    def release(self):
        pass
    def add(self):
        pass

class   Animal(Structure,Human):
    

    def __init__(self,name,food,origin,kind,date,location,age,status,ID,gender,section,accomodation):

        Human.__init__(self,name,date,location,age,status,ID,gender):          
        

        Structure.__init__(self,name,location,section,date,accomodation):


    def sound(self):
        pass
    def pic_shot(self):
        pass

    def feed(self):

class Staff(Human,Structure):
    
    def __init__(self,name,date,location,age,status,position,ID,gender,section,accomodation):

            
        Human.__init__(self,name,date,location,age,status,ID,gender):          
        

        Structure.__init__(self,name,location,section,date,accomodation):
            
    def promote(self):
        pass
    def demote (self):
        pass
    def pay(self):
        pass
    def work(self):
        pass
    

class Tourist(Human):

    def __init__(self,name,date,location,age,status,ID,gender,ammount):

        Human.__init__(self,name,date,location,age,status,ID,gender):

    def charge(self):
        pass
    
    
