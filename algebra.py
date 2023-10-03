def calculate_algebra(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

# Example usage:
expression = "2 * (3 + 4)"
result = calculate_algebra(expression)
print(f"The result of '{expression}' is: {result}")
