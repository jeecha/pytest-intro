def calculator(operation, a, b):
    if operation == "sum":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        raise ValueError("unknown operation")

# write the test cases for above method
