# Budget App

A budget category class to track deposits, withdrawals, and transfers.

## Class
`Category(name)`

## Methods
- `deposit(amount, description)`: Add money
- `withdraw(amount, description)`: Spend money
- `transfer(amount, category)`: Transfer between categories
- `get_balance()`: Get current balance
- `__str__()`: Print a formatted ledger

## Function
`create_spend_chart(categories)`: Creates a bar chart of spending by category

## Example
```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
