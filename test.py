settings = {
    'lower': True,
    'upper': True,
    'symbols': True,
    'numbers': True,
    'space': False,
    'length': 8
}

choices = list(filter(lambda key: settings[key] == True, settings.keys()))
print(choices)