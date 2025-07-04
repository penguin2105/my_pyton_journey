def calculate_total(cart, age):
    total = sum(item['price'] for item in cart)
    if age >= 60:  
        total *= 0.9 
    return total

def mail():
    cart = []
    while True:
        name = input("Товар( 'стоп') : ")
        if name.lower() == "стоп":
            break
        price = float(input("Цена: "))
        cart.append({"name": name, "price": price})
    
    age = int(input("Ваш возраст: "))
    total = calculate_total(cart, age)
    
    print("\nЧек:")  
    for item in cart:
        print(f"- {item['name']}: {item['price']} руб")
    print(f"Итого с учетом скидки: {total:.2f} руб")

if __name__ == "__main__":
    mail()

            