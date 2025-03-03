# -Store-Calculator
🐍 Python Project: Simple Store Calculator
💡 Project Idea:
We will create a simple store calculator where the user enters product names, prices, and quantities. The program will then calculate the total cost and display a receipt.

📌 Steps to Follow:
Use variables to store product names, prices, and quantities.
Perform mathematical operations to calculate the total bill.
Use input and output functions to interact with the user.
Format the output to display a clear and structured receipt.

### 🐍 **Python Project: Simple Store Calculator**  

💡 **Project Idea:**  
We will create a simple store calculator where the user enters product names, prices, and quantities. The program will then calculate the total cost and display a receipt.  

---

### **📌 Steps to Follow:**
1. Use **variables** to store product names, prices, and quantities.  
2. Perform **mathematical operations** to calculate the total bill.  
3. Use **input and output** functions to interact with the user.  
4. Format the output to display a **clear and structured receipt**.  

---

### **✍️ Python Code:**
```python
# 🛒 Simple Store Calculator

# Get the first product details
product1 = input("Enter the name of the first product: ")
price1 = float(input(f"Enter the price of {product1}: "))
quantity1 = int(input(f"Enter the quantity of {product1}: "))

# Get the second product details
product2 = input("Enter the name of the second product: ")
price2 = float(input(f"Enter the price of {product2}: "))
quantity2 = int(input(f"Enter the quantity of {product2}: "))

# Calculate total cost for each product
total1 = price1 * quantity1
total2 = price2 * quantity2

# Calculate grand total
grand_total = total1 + total2

# Display the receipt
print("\n🧾 *** RECEIPT ***")
print(f"{product1}: {quantity1} × {price1} = {total1} currency units")
print(f"{product2}: {quantity2} × {price2} = {total2} currency units")
print("---------------------------")
print(f"💰 Grand Total: {grand_total} currency units")
```

---

### **🎯 What Will You Learn?**
✅ How to use **variables** to store data.  
✅ How to work with **different data types** (strings, floats, integers).  
✅ How to perform **basic mathematical operations** (multiplication, addition).  
✅ How to use **input and output** to make an interactive program.  

🔹 **Bonus Challenge:**  
- Add a **10% discount** if the total cost is greater than 100.  
- Allow the user to enter **more than two products** using **lists**.  

🚀 **Try it and let me know how it works!** ✨