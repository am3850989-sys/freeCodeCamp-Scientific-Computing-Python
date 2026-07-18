# Tower of Hanoi

This project implements a solution to the Tower of Hanoi problem using recursion.

## Description
The program solves the Tower of Hanoi puzzle for n disks and records every state of the rods.
It moves disks from rod A to rod C using rod B as auxiliary, following the rules:
1. Only one disk can be moved at a time
2. A larger disk cannot be placed on top of a smaller disk

## Functions
- `hanoi_solver(n)`: Solves the puzzle for n disks and returns all states as a string
- `move(n, source, target, auxiliary)`: Recursive function to move disks
- `record_state()`: Saves the current state of all rods

## How to Run
Run `main.py` to see the solution for 3 disks. Change the number in `hanoi_solver(3)` to test with more disks.
