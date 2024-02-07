class Computer:

    # What attributes will it need?
    #description, price, hard drive, memory, operating system, processor, year made, computer ID
    # How will you set up your constructor?
    ## I will set up the constructor by calling def __init__(self, (needed attributes))
    # need to determine if string, int, float etc.
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description:str, price:float, hard_drive_capacity:int, memory:int, operating_system:str, processor_type:str, year_made:int):
        self.description = description
        self.price = price
        self.hard_drive_capacity = hard_drive_capacity 
        self.memory = memory
        self.operating_system = operating_system
        self.processor_type = processor_type
        self.year_made = year_made

    # What methods will you need?
    # The methods that would be in class computer are updating the operating system.
   
    def update_operating_system(self, new_os):
        self.operating_system = new_os
