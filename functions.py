def factorial(n):
    #   return n!
    if n == 0:        
        return 1
    else:             
        return n * factorial(n-1)
def fibonacci(n):
    #   return the nth Fibonacci number
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def is_prime(n):
    #   return True if n is prime, False otherwise
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def get_grade (score):
    #   return the letter grade for a given score
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
def is_palindrome(word):
    # return True or False
    return word == word[::-1]
print(factorial(5))      
print(fibonacci(6))      
print(is_prime(7))       
print(get_grade(95))     
print(is_palindrome("racecar"))