def solve(meal_cost, tip_percent, tax_percent):
    meal_cost = float(meal_cost)
    tip_percent = int(tip_percent)
    tax_percent = int(tax_percent)
    print(meal_cost)
    tip_percent = (tip_percent/100.)*meal_cost
    print(tip_percent)
    tax_percent = (tax_percent/100.)*meal_cost
    totalCost = int(round(meal_cost+tip_percent+tax_percent))
    print("The total meal cost is", totalCost, "dollars.")


solve(10,2,3)