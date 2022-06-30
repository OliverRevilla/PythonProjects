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

#Write a Python program to check the nth-1 string is a proper substring 
#of nth string in a given list of strings

    def exercise_five(string_list):
        # to know if one substring is inside of another one it use in function
        return string_list[-2] in string_list[-1]

#Write a Python program to test a list of one hundred integers between 0 and 999,
#which all differ by ten from one another. Return true or false.
    
    def exercise_six(numbers):
        last_element = numbers[0]
        if len(numbers < 100):
            return False
        else:
            for pos in range(1, len(numbers)):
                if last_element + 10 == numbers[pos]:
                    last_element = numbers[pos]
                else:
                    return False

        return True

# Write a python program to check a given list of integers where
# the sum of the first i integers is i.
    def exercise_seven(numbers):
        return numbers[0] == 1

#Write a Python program to split a string of words separated by commas
# and spaces into two lists, words and separators.
    def exercise_eight(string_list):
        import re
        c = []
        d = re.split(r"([ ,]+)", string_list)
        for word in string_list:
            if word in (' ',',','," "'):
                c.append(word)
        for word in d:
            if word in (' ',','):
                d.remove(word)
        print([d,c])

#Given a string consisting of whitespace and groups of matched parentheses,
# write a Python program to split it into groups of perfectly matched parentheses
# without any whitespace.

    def exercise_ten(string_list):
        match = ''
        matches = []
        for c in string_list.replace(" ",""):
           match = match + c
           if match.count('(') == match.count(')'):
                matches.append(match)
                match = ''
        return matches

print(Exercises.exercise_ten("() (( ( )() ( )) ) ( ())"))





