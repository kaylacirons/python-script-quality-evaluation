"""
Sample Python Scripts

This file includes multiple scripts with varying levels of
code quality, clarity, and efficiency.
"""

def sum_numbers(nums):
    total = 0
    for i in range(len(nums)):
        total = total + nums[i]
    return total


def get_even_numbers(numbers):
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return evens


def reverse_string(text):
    reversed_text = ""
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]
    return reversed_text


def check_palindrome(word):
    return word == word[::-1]
