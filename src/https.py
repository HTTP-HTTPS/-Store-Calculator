print('🛒 Store Calculator')
# Get product details
produit = input('Enter Name of the product: ')
price = float(input('Enter The Price of the product: '))
quantity = int(input('Enter The Quantity of the product: '))

# Calculate total
total = price * quantity

# Display the receipt
print('\n###### 🧾 Receipt ######')
print(f'Product  : {produit}')
print(f'Price    : {price:.2f} DH')
print(f'Quantity : {quantity}')
print(f'Total    : {total:.2f} DH')
print('#########################')
print('🛒 Thank you for shopping with us!')