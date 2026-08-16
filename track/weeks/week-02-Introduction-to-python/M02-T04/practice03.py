# Calculate an invoice total using a function

# defining the function to display the total invoice
def display_invoice_total(price, quantity): 
    # Write your code here
    total = price * quantity
    print(f"Total: {total}")

# reading the inputs
price = int(input()) 
quantity = int(input())

# calling the function
display_invoice_total(price, quantity)