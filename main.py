from checkoutApp import CheckOut, PricingRule

pricing_rules = {
    'A': PricingRule(unit_price=50, special_price={'quantity': 3, 'price': 130}),
    'B': PricingRule(unit_price=30, special_price={'quantity': 2, 'price': 50}),
    'C': PricingRule(unit_price=20),
    'D': PricingRule(unit_price=15),
}

co = CheckOut(pricing_rules)


# Scenarios from the task in mail

# Scenario 1: A, B $80
print("\nScenario #1")
co.scan('A')
co.scan('B')
co.showCart()
total_price = co.total()
print(f'Cart Total: ${total_price}')
co.purge()

# Scenario 2: A, A $100
print("\nScenario #2")
co.scan('A')
co.scan('A')
co.showCart()
total_price = co.total()
print(f'Cart Total: ${total_price}')
co.purge()

# Scenario 3: A, A, A $130
print("\nScenario #3")
co.scan('A')
co.scan('A')
co.scan('A')
co.showCart()
total_price = co.total()
print(f'Cart Total: ${total_price}')


# To discard an added item
# co.discard('A')
