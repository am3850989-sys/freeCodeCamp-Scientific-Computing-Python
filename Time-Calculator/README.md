# Time Calculator

Adds a duration to a start time and handles days later.

## Function
`add_time(start, duration, day_of_week=None)`

## Features
- 12-hour clock format AM/PM
- Handles crossing days and multiple days later
- Optional: Takes starting day of the week

## Example
`add_time("3:00 PM", "3:10", "Monday")`
Output: `6:10 PM, Monday`
