from checkoutApp import CheckOut, PricingRule


def test_scan_single_item():
    pricing_rules = {'A': PricingRule(unit_price=50)}
    co = CheckOut(pricing_rules)
    co.scan('A')
    assert co.total() == 50


def test_scan_multiple_items():
    pricing_rules = {'A': PricingRule(
        unit_price=50), 'B': PricingRule(unit_price=30)}
    co = CheckOut(pricing_rules)
    co.scan('A')
    co.scan('B')
    assert co.total() == 80


def test_scan_item_with_special_price():
    pricing_rules = {'A': PricingRule(
        unit_price=50, special_price={'quantity': 3, 'price': 130})}
    co = CheckOut(pricing_rules)
    co.scan('A')
    co.scan('A')
    co.scan('A')
    assert co.total() == 130


def test_scan_item_without_pricing_rule():
    pricing_rules = {'A': PricingRule(unit_price=50)}
    co = CheckOut(pricing_rules)
    co.scan('B')  # 'B' doesn't have a pricing rule
    assert co.total() == 0


def test_scan_item_with_special_price_and_regular_price():
    pricing_rules = {'A': PricingRule(
        unit_price=50, special_price={'quantity': 3, 'price': 130})}
    co = CheckOut(pricing_rules)
    co.scan('A')
    co.scan('A')
    co.scan('A')
    co.scan('A')  # Additional 'A' without special price
    assert co.total() == 180


def test_scan_item_with_special_price_multiple_times():
    pricing_rules = {'A': PricingRule(
        unit_price=50, special_price={'quantity': 3, 'price': 130})}
    co = CheckOut(pricing_rules)
    co.scan('A')
    co.scan('A')
    co.scan('A')
    co.scan('A')
    co.scan('A')
    assert co.total() == 230


def test_empty_cart():
    pricing_rules = {'A': PricingRule(unit_price=50)}
    co = CheckOut(pricing_rules)
    assert co.total() == 0


def test_discard():
    pricing_rules = {
        'A': PricingRule(unit_price=50, special_price={'quantity': 3, 'price': 130}),
        'B': PricingRule(unit_price=30, special_price={'quantity': 2, 'price': 50}),
    }
    co = CheckOut(pricing_rules)
    co.scan('A')
    co.scan('B')
    co.scan('A')
    co.discard('A')
    assert co.total() == 80


def test_prune():
    pricing_rules = {
        'A': PricingRule(unit_price=50, special_price={'quantity': 3, 'price': 130}),
        'B': PricingRule(unit_price=30, special_price={'quantity': 2, 'price': 50}),
    }
    co = CheckOut(pricing_rules)
    co.scan('A')
    co.scan('B')
    co.purge()
    assert co.cart == {}
