def sayhello(name=None, withemoji=None):
    if withemoji == None or withemoji == False:
        if name == None:
            return 'Hello, world!'
        elif name != None:
            return f'Hello, {name}!'
    elif withemoji == True:
        if name == None:
            return 'Hello, world! 🌎'
        elif name != None:
            return f'Hello, {name}! 🌎'

def say_hello(name=None, withemoji=None):
    if withemoji == None or withemoji == False:
        if name == None:
            sayhello()
        elif name != None:
            sayhello(name)
    elif withemoji == True:      
        if name == None:
            sayhello(withemoji=True)
        elif name != None:
            sayhello(name, withemoji=True)