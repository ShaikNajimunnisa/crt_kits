class Customer:
    def __init__(self):
        pass
#mutator or setter method
    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def set_age(self, age):
        self.age = age
        #Accessor or getter method
    def get_name(self):
        print(f"name is  {self.name}")
    def get_id(self):
        print(f"id is  {self.id}")
    def get_age(self):
        print(f"age is  {self.age}")
         
        