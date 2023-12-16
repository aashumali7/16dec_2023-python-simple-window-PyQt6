#1. function defination is one time process
def hello(std = "aashu"): #formal argument (std with default argument)
    print(f"hello {std}")
    pass


#2. function calling/Invoking is many time process
hello('aashish') #actual argument
hello('anil') 
hello() #calling function without argument