
#question 1
Fibonacci = lambda n: (lambda f: f(f, n))(lambda self, n, a=0, b=1: [a] + self(self, n-1, b, a+b) if n > 1 else [a])

print(Fibonacci(8))
#for x in :
#print(x)

lambda x,y : x*y

#question 2
concat_strings = lambda lst: lst[0] + ' ' + concat_strings(lst[1:]) if len(lst) > 1 else lst[0]
result = concat_strings([ "this", "is", "our", "final", "project"])
print(result)



#question 3
from functools import reduce
#cumulative_sum_of_squares = lambda lst: list(map(lambda sublist: reduce(lambda acc, x: acc + (x**2 if x % 2 == 0 else 0), sublist, 0), lst))

#cumulative_sum_of_squares = lambda lst: [reduce(lambda acc, x: acc + (x**2 if x % 2 == 0 else 0), sublist, 0) for sublist in lst]


cumulative_sum_of_squares = lambda lst: (
    lambda f: f(f, lst)
)(
    lambda self, lst: (
        lambda map_reduce: list(map(map_reduce, lst))
    )(
        lambda sublist: (
            reduce(
                lambda acc, x: acc + (x**2 if x % 2 == 0 else 0),
                sublist,
                0
            )
        )
    )
)

# Example usage
input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
result = cumulative_sum_of_squares(input_list)
print(result)


#question 4
def cumulative_op(binary_op):
 return lambda sequence: reduce(binary_op, sequence)


#cumulative_op= lambda binary_op:  lambda sequence: reduce(binary_op, sequence)

# Example usage
# Factorial implementation
factorial = cumulative_op(lambda x, y: x * y)

# Exponentiation implementation
exponentiation = cumulative_op(lambda x, y: x ** y)

# Test cases
print(factorial(range(1, 6)))
print(exponentiation([2, 3, 2]))




#question 5

nums = [1, 2, 3, 4, 5, 6]
sum_squared = reduce(lambda acc, x: acc + x, map(lambda x: x**2, filter(lambda num: num % 2 == 0, nums)))
print(sum_squared)




#question 6
count_palindromes = lambda lst: list(map(lambda sublist: reduce(lambda acc, s: acc + (s == s[::-1]), sublist, 0), lst))

# Example usage
input_list = [["racecar", "hello", "level"], ["madam", "world"], ["noon", "radar", "python"]]
print(count_palindromes(input_list))



#question 7
def generate_values():
 print('Generating values...')
 yield 1
 yield 2
 yield 3

def square(x):
 print(f'Squaring {x}')
 return x * x


print('Eager evaluation:')
values = list(generate_values())
squared_values = [square(x) for x in values]
print(squared_values)

#הפונקציה generate_values נקראת ותוצאותיה נאספות לרשימה באמצעות list(generate_values()).
# זה מאלץ יצירה של כל הערכים מראש, כלומר יש הקצאת זכרון לכל הערכים ברשימה לפני שמשתמשים בהם בפונקציה הבאה.

print('\nLazy evaluation:')
squared_values = [square(x) for x in generate_values()]
print(squared_values)
# בשיטת Lazy evaluation
# הערכים לא מחושבים עד שהם באמת נדרשים. כאן, generate_values
# לא מחשבת את כל הערכים מראש אלא מייצרת אותם אחד אחרי השני
# מה שמוביל לחיסכון פוטנציאלי בזיכרון ובחישוב.



#question 8

primes_descending = lambda lst: sorted([x for x in lst if all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1], reverse=True)
numbers = [10, 15, 2, 7, 19, 23]
print(primes_descending(numbers))
