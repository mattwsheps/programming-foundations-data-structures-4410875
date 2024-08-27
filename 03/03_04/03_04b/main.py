user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    updated_pref = {}
    for key, value in user_preferences.items():
        if value != None:
            updated_pref[key] = value
    return updated_pref


print(update_preferences(user_preferences))
