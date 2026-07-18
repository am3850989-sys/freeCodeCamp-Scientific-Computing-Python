class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.balance

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
        total = f"Total: {self.balance:.2f}"
        return title + items + total


def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(spent)

    total_spent = sum(spent_amounts)
    percentages = [int((spent / total_spent) * 100 // 10 * 10) for spent in spent_amounts]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in percentages:
            chart += "o " if percent >= i else " "
        chart += "\n"
    
    chart += " " + "-" * (len(categories) * 3 + 1) + "\n"
    
    names = [category.name for category in categories]
    max_len = max(len(name) for name in names)
    for i in range(max_len):
        chart += " "
        for name in names:
            chart += name[i] + " " if i < len(name) else " "
        if i < max_len - 1:
            chart += "\n"
    return chart
