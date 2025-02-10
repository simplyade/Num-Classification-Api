def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_armstrong(number: int) -> bool:
    num_str = str(number)
    num_len = len(num_str)
    return sum(int(digit) ** num_len for digit in num_str) == number

def classify_number(number: int) -> dict:
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")
    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": False,  # Placeholder for perfect number logic
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(number)),
    }