# This is the main module to run and test everything from 

import budget_category

food_category = budget_category.BudgetCategory('Food', 500)
food_category.add_expense(100)
food_category.display_category_summary() 

entertainment_category = budget_category.BudgetCategory('Entertainment', 1000)
entertainment_category.add_expense(300)
entertainment_category.display_category_summary()