class AgeError(Exception):
    pass

class ScoreError(Exception):
    pass

class NegativeAmountError(Exception):
    pass

def validate_age(age):
    if age < 0 or age > 150:
        raise AgeError(f"Invalid age: {age}. Must be 0-150.")
    return f"Valid age: {age}"

def validate_score(score):
    if score < 0 or score > 100:
        raise ScoreError(f"Invalid score: {score}. Must be 0-100.")
    return f"Valid score: {score}"

def validate_amount(amount):
    if amount < 0:
        raise NegativeAmountError(f"Amount cannot be negative: {amount}")
    return f"Valid amount: {amount}"

if __name__ == "__main__":
    try:
        print(validate_age(25))
        print(validate_score(85))
        print(validate_amount(100))
        
        # Uncomment to test exceptions
        # print(validate_age(-5))
        # print(validate_score(150))
        # print(validate_amount(-50))
        
    except (AgeError, ScoreError, NegativeAmountError) as e:
        print(f"Error: {e}")    