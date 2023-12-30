from typing import Dict
from utils.logger import log
from tabulate import tabulate


class PricingRule:
    def __init__(self, unit_price: int, special_price: Dict[str, int] = None):
        """Allows user to add pricing rules to products

        Args:
            unit_price (int): Number of units required to apply this price
            special_price (Dict[str, int], optional): The special price that will be applied to these units. Defaults to None.
        """
        self.unit_price = unit_price
        self.special_price = special_price or {}


class CheckOut:

    def __init__(self, pricing_rules: Dict[str, PricingRule]):
        """Constructor for Checkout

        Args:
            pricing_rules (Dict[str, PricingRule]): Configuration for the checkout constructor
        """
        self.pricing_rules = pricing_rules
        self.cart = {}

    def scan(self, item: str):
        """Adds item to the cart

        Args:
            item (str): Name of the item to add to cart
        """

        # Check if item is valid(has price)
        if item not in self.pricing_rules:
            log.error(
                f"Item {item} can not be added. It does not have price listed in pricing rules")
            return

        if item not in self.cart:
            self.cart[item] = 1
        else:
            self.cart[item] += 1
        log.info(f"Item {item} added to cart!")

    def showCart(self):
        """Shows the current cart in tabular format
        """
        headers = ["Item", "Quantity"]
        print(
            tabulate([[k, v] for k, v in self.cart.items()], headers=headers, tablefmt="grid"))

    def discard(self, item: str):
        """Discards(remove) the item from the cart

        Args:
            item (str): Name of the item to discard from cart
        """
        if item in self.cart:
            self.cart[item] -= 1
            # delete the item if the quantity is zero now
            if self.cart[item] == 0:
                del self.cart[item]
            log.info(f"Item {item} removed from cart!")

    def purge(self):
        """Removes all the items from the cart.
        """
        self.cart = {}

    def total(self):
        """Calculates the total of all the items in the cart

        Returns:
            int: Total price of items in the cart
        """
        total_price = 0
        for item, quantity in self.cart.items():
            total_price += self.calculate_item_price(item, quantity)
        return total_price

    def calculate_item_price(self, item: str, quantity: int):
        """Calculates the item prices on the basis of rules

        Args:
            item (str): Name of the item
            quantity (int): Quantity of the items

        Returns:
            int: Total price of this item in the cart
        """

        # Check if it has special pricing
        if self.pricing_rules[item].special_price:
            # This has special pricing, apply it
            singleItems = quantity % self.pricing_rules[item].special_price['quantity']
            # Group the items with the pricing values
            groupedItems = (
                quantity // self.pricing_rules[item].special_price['quantity'])
            log.info(
                f"For item {item}, there are {groupedItems} grouped discount and {singleItems} standard price applied")
            return (groupedItems*self.pricing_rules[item].special_price['price'])+(singleItems*self.pricing_rules[item].unit_price)
        else:
            return quantity*self.pricing_rules[item].unit_price
