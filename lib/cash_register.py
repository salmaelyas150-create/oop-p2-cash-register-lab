
class CashRegister:
    """A cash register that tracks items, discounts, and transactions."""

    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []
        self.discount = discount

    @property
    def discount(self):
        """Return the current discount percentage."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """Validate that the discount is an integer between 0 and 100."""
        if type(value) is int and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            if not hasattr(self, "_discount"):
                self._discount = 0

    def add_item(self, item, price, quantity=1):
        """Add an item, update the total, and record the transaction."""
        self.total += price * quantity
        self.items.extend([item] * quantity)

        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity,
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        """Apply the discount percentage to the total."""
        if self.discount == 0 or not self.previous_transactions:
            print("There is no discount to apply.")
            return

        self.total = self.total * (100 - self.discount) / 100
        print(f"After the discount, the total comes to ${self.total:g}.")

    def void_last_transaction(self):
        """Remove the last transaction and update the total and items."""
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        transaction = self.previous_transactions.pop()

        item = transaction["item"]
        price = transaction["price"]
        quantity = transaction["quantity"]

        self.total -= price * quantity

        for _ in range(quantity):
            self.items.remove(item)

        if not self.previous_transactions:
            self.total = 0.0




