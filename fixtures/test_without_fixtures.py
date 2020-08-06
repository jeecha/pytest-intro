def resource():
    return "i am the resource"

def test():
    res = resource()

def test2():
    res = resource()

# Here we have some test cases, which all require some resource,
# like database or server connection.
