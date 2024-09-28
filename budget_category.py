# Module for Budget class and methods 

class BudgetCategory:      # BudgetCategory class with attributes 'category_name' and 'allocated_budget' 
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        
    def get_category_name(self):      # getter for 'category_name' 
        return self.__category_name 
    
    def set_category_name(self, new_name):   # setter for 'category_name' 
        self.__category_name = new_name 
    
    def get_budget(self):      # getter for 'allocated_budget'
        return self.__allocated_budget
    
    def set_budget(self, new_budget):      # setter for 'allocated_budget' 
        if new_budget > 0:
            return self.__allocated_budget == new_budget   # returns new_budget only if new_budget is positive 
        else:
            print("Error, invalid budget amount.") 
            
    def add_expense(self, amount):
        try:
            if amount <= self.__allocated_budget: # if amount of expense is less than budget for category
                self.__allocated_budget = self.__allocated_budget - amount   
        except Exception as e:
            print(f"Error: {e}")
    
    def display_category_summary(self):
        print(f"Current budget for {self.get_category_name()}: {self.get_budget()}") 
    