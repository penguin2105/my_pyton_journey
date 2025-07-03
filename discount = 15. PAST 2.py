def calculate_discount(price, age, is_regular=False):
    if age >= 60:  
        return price * 0.7
    elif is_regular:  
        return price * 0.85
    else:
        return price


print(calculate_discount(1000, 25))  
print(calculate_discount(20000, 65))  
print(calculate_discount(110000, 30, True))  