"""Task AI 4 Climate 

Q2/Write a program to find all prime numbers up to a given range of numbers? 
"""
from typing import Iterator


def is_prime(number: int) -> bool:
    """Check number is prime"""

    for i in range(2, number):
        if (number%i) == 0: 

            return False

    return True


def find_prime_numbers_in_range(start_range: int, end_range: int) -> Iterator[int]:
    """Find all prime numbers in range of numbers"""

    for number in range(start_range, end_range + 1):
        if number > 1 and is_prime(number):
            yield number


if __name__ == "__main__":
    
    prime_numbers = find_prime_numbers_in_range(1, 10)
    print("Oh No,  ^_*", list(prime_numbers))

