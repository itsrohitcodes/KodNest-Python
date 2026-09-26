# Group Orders according to thier Customer ID

def group_orders(orders):
    orders_by_customer = {}

    # Write your grouping logic here
    for order_id, customer_id in orders:
        if customer_id not in orders_by_customer:
            orders_by_customer[customer_id] = []
        orders_by_customer[customer_id].append(order_id)

    return orders_by_customer


n = int(input())
orders = []

for _ in range(n):
    order_id, customer_id = input().split()
    orders.append((order_id, customer_id))

orders_by_customer = group_orders(orders)

for customer_id, order_ids in orders_by_customer.items():
    print(customer_id + ": " + " ".join(order_ids))