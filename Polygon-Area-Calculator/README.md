```markdown
# Polygon Area Calculator

Classes for working with Rectangles and Squares.

## Classes
`Rectangle(width, height)`  
`Square(side)` inherits from Rectangle

## Methods
- `get_area()`: Returns area
- `get_perimeter()`: Returns perimeter  
- `get_diagonal()`: Returns diagonal
- `get_picture()`: Returns string picture of shape
- `get_amount_inside(shape)`: How many of the passed shape fit inside
- `set_width()`, `set_height()`, `set_side()`: Setters

## Example
```python
rect = Rectangle(10, 5)
print(rect.get_area()) # 50
