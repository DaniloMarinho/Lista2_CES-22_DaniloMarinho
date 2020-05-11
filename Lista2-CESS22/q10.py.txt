def tellName(name):
    return "ola {0}".format(name)

def startCapitalLetter(func):
    def dec(name):
        return func(name).capitalize()
    return dec

given_name = startCapitalLetter(tellName)

print given_name("John")