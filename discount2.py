#Question 2
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompting the user for input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Calculating the final price
final_price = calculate_discount(original_price, discount)

# Printing the result
if discount >= 20:
    print(f"The final price after a {discount}% discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {original_price}")