

from ast import Return


class Exercises:
    def __init__(self):
        pass

# Write a Python program find a list of integers with exactly 
# two occurrences of nineteen and at least three occurrences of five.
    def exercise_one(numbers):
        return  numbers.count(19) == 2 and numbers.count(5) >= 3

#We are making n stone piles! The first pile has n stones.
#If n is even, then all piles have an even number of stones.
#If n is odd, all piles have an odd number of stones.
#Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.
    def exercise_four(number):
        from functools import reduce
        lista = [range(number, number*2)]
        return (reduce(lambda x: x + 2, lista))


"""
Write a Python program to check the nth-1 string is a proper substring 
of nth string in a given list of strings
"""
    def 






            





