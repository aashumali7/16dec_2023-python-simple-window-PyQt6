#1 class defination 
class Country():
    #1.1 property/variable
    name=''
    capital=''

    #1.2 constructor/special function
    def __init__(self,c,n):
        #the role of constructor is to initialize the properties
        self.name= n 
        self.capital= c
    pass
    #1.3 method/function
    def displayDetail(self):
        print(f'{self.capital} is the capital of {self.name}') 
    
    pass
#2. Create classobject / create Instance of the class
#classobject = ClassName()
co = Country(n='India',c="Delhi") #keyword argument
#classobject.method 
co.displayDetail()