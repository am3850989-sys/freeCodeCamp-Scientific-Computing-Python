# User Configuration Manager

This project implements a simple user configuration manager using Python dictionaries.

## Description
The program allows users to manage application settings with basic CRUD operations:
- **Create**: Add new settings
- **Read**: View all current settings  
- **Update**: Modify existing settings
- **Delete**: Remove settings

All setting keys and values are automatically converted to lowercase for consistency.

## Functions

- `add_setting(settings, new_setting)`: Adds a new setting if it doesn't already exist
- `update_setting(settings, new_setting)
