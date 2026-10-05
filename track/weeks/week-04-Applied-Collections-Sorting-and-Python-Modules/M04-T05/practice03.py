# Use a module with an alias

import math as m

number = 100
decimal_number = 9.3

square_root = m.sqrt(number)
rounded_up = m.ceil(decimal_number)
rounded_down = m.floor(decimal_number)

print("Square Root:", square_root)
print("Rounded Up:", rounded_up)
print("Rounded Down:", rounded_down)