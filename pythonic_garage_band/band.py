from abc import ABC, abstractmethod

class Band:
    instances = []


    def __init__(self, band_name, members=[]):
        """
        Method which creates name of the band and its members
        """
        self.name = band_name
        self.members = members
        self.instances.append(self)


    def play_solos(self):
        """
        Returns list that represents all members of the band playing their solos based on the
        order they were added to the band
        """
        solos = map(lambda members: members.play_solo(), self.members)
        return list(solos)


    def __str__(self):
        """string with the "name" of the obj instance"""

        return ( self.name)

    def __repr__(self):
        """string with the "name" of the obj instance"""

        return ( self.name)

    @classmethod
    def to_list(cls):
        """Returns all Band instances that were created"""
        return cls.instances

class Musician(ABC) :
     members = []

     def __init__(self, role):
        self.role = role
        self.members.append(self)

     def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    

     def __repr__ (self):
          return f"Guitarist instance. Name = {self.name}"

     def play_solo(self):
        pass

     def get_instrument(self):
        return f"{self.instrument}"


class Guitarist(Musician):
     def __init__(self,name):
        self.name=name
        

     def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    

     def __repr__ (self):
          return f"Guitarist instance. Name = {self.name}"
    
     def get_instrument(self):
          return "guitar"

     def play_solo(self):
          return "face melting guitar solo"
 
class Drummer(Musician):
     def __init__(self,name):
        self.name=name
     def __str__(self):
          return f"My name is {self.name} and I play {self.get_instrument()}"
    

     def __repr__ (self):
          return f"Drummer instance. Name = {self.name}"
     def get_instrument(self):
         return "drums"

     def play_solo(self):
          return "rattle boom crash"

class Bassist (Musician):
     def __init__(self,name):
        self.name=name

     def __str__(self):
          return f"My name is {self.name} and I play {self.get_instrument()}"

     def __repr__ (self):
          return f"Bassist instance. Name = {self.name}"
     
     def get_instrument(self):
          return "bass"

     def play_solo (self):
           return "bom bom buh bom"

if __name__=="__main__":
     dina = Guitarist('Dina Shboul')
     qasem = Drummer('Qasem Shoul')
     lolo = Bassist('Lolo Shboul')
    
     band = Band('Rab', [dina, lolo, qasem])  
     print(band.to_list())
     print('Mom :',dina)
     print(dina.play_solo())
     print(dina.get_instrument())