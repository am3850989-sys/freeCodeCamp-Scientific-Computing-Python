test_settings = {"theme" :"light"}

def add_setting(settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings,new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()

    if key not in settings :
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(settings, key):
    key = key.lower()

    if key not in settings :
        return "Setting not found!"

    del settings[key]
    return f"Setting '{key}' deleted successfully!"

def view_settings(settings):
    if not settings:
        return "No settings available."

    results = "Current User Settings:\n"
    for key, value in settings.items():
        results += f"{key.capitalize()}: {value}\n"

    return results

# للتجربة
print(add_setting(test_settings, ("Volume", "High")))
print(update_setting(test_settings, ("Theme", "Dark")))
print(delete_setting(test_settings, "volume"))
print(view_settings(test_settings))
