# part 1

#1. Create a Rectangle class with attributes length and width. 
#Add methods to calculate the area and perimeter of the rectangle. 

#class Rectangle:
 #   def __init__(self, lengh, width):
  #      self.lengh = lengh
   #     self.width = width
    
    #def area(self):
     #   return self.lengh * self.width
    
    #def perimeter(self):
     #   return 2 * (self.lengh + self.width)
    
#rect = Rectangle (5, 10)

#print(rect.area())
#print(rect.perimeter())

# part 2

#2. Create a BankAccount class with attributes account_number and balance. 
#Add methods to deposit and withdraw money from the account. 

#class Bank_Account:
 #   def __init__(self, account_number, balance):
  #      self.account_number = account_number
   #     self.balance = balance

    #def deposit(self, amount):
     #   if amount > 0:
      #      self.balance += amount
       #     return f"Deposited {amount}.  New balance: {self.balance:.2f}"
        #else:
         #   return "Invalid amount"
        
    #def withdraw(self, amount):
     #   if amount > 0 and amount <= self.balance:
      #      self.balance -= amount
       #     return f"Withdraw £{amount}. New balance: {self.balance:.2f}"
        #else:
         #   return "Invalid amount or insufficient funds"

#account = Bank_Account(101010, 1000)

#print(account.deposit(1000))
#print(account.withdraw(500))


# Part 3

#3. Create a Car class with attributes make, model, and year. 
#Add methods to get and set the values of the attributes.

#class Cars:
    #def __init__ (self, make, model, year):
     #   self.make = make
      #  self.model = model
       # self.year = year

   # def get_make(self):
    #    return self.make
    
    #def set_make(self, make):
        #self.make = make

    #def get_model(self):
     #   return self.model
    
    #def set_model(self, model):
       # self.model = model

    #def get_year(self):
     #   return self.year
    
    #def set_year(self, year):
       # return self.year
    
# Create a Car object    
#my_car = Cars("Toyota", "Corolla", 2015)

# Get the attributes
#print(f"Make: {my_car.make}")
#print(f"Model: {my_car.model}")
#print(f"Year: {my_car.year}")

# Set new values for the attributes
#my_car.make = "Jeep"
#my_car.model = "Renegade"
#my_car.year = 2017

# Get the updated attributes
#print(f"Make: {my_car.make}")
#print(f"Model: {my_car.model}")
#print(f"Year: {my_car.year}")

# Part 4

#4. Create a Product class with attributes name, price, and quantity. 
#Add methods to calculate the total value of the product (price * quantity) 
#and add or remove items from the product inventory. 

class Product:
    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity
    
    def add_item(self, quantity_to_add):
        if quantity_to_add > 0:
            self.quantity += quantity_to_add
            return f"Added {quantity_to_add} {self.name}, new quantity: {self.quantity}"
        else:
            return "Quantity must be grater than 0"
        
    def remove_item(self, quantity_to_remove):
        if 0 < quantity_to_remove <= self.quantity:
            self.quantity -= quantity_to_remove
            return f"Removed {quantity_to_remove} {self.name}, new quantity: {self.quantity}"
        else:
            return "Invalid quantity or insufficient"
        
product_1 = Product("watch", 100.00, 50)

print(f"total value of {product_1.name}: £{product_1.calculate_total():.2f}")

# Add and remove items from the product inventory
print(product_1.add_item(25))
print(product_1.remove_item(15))
print(product_1.remove_item(100))

print(f"total value of {product_1.name}: £{product_1.calculate_total():.2f}")






