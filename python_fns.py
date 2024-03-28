def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    discounted_price = price - (price * discount_percent / 100)
    return discounted_price
  else:
    return price

#Get user input for original price and discount percentage  
original_price = float(input("enter the original price of the item:"))
discount_percent = float(input("Enter the discount percentage: "))

#calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

#print the final price
if final_price != original_price:
  print(f"The final price after applying a {discount_percent}% discount is: ${final_price: }")
else:
  print("No discount applied. The original price is: ${:.2f}".format(original_price))  
