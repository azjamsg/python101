def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return tax
    
price = value_added_tax(100)    
print(price)
