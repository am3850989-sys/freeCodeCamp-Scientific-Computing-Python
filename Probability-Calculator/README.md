```markdown
# Probability Calculator

Estimates probability by running experiments with a hat of colored balls.

## Class
`Hat(**kwargs)`  
Example: `Hat(red=3, blue=2)`

## Methods
- `draw(num_balls)`: Removes and returns balls at random

## Function  
`experiment(hat, expected_balls, num_experiments)`

## Example
```python
hat = Hat(red=5, blue=2)
probability = experiment(hat, {"red": 2, "blue": 1}, 2000)
