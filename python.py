from numpy import prod, square

x = max(5, 8, 9, 10, 50)
print(x)



l = sum([10, 20, 30, 40, 50])
print(l)



m = prod([4, 8])
print(m)



range_1 = range(0, 20, 1)
number = int(input('Enter a number : '))
 
if number in range_1 :
    print(number, 'is present in the range.')
else :
    print(number, 'is not present in the range.')



def my_outer_function():
    print("Hello from my outer function")

    def my_inner_function():
        print("Hi there from my inner function!")
        print("another message")
    return my_inner_function

my_inner = my_outer_function()
my_inner()



'set' is a built in which get the unique items in a list (array).

numbers = [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9, 10, ]


def get_unique_numbers(numbers):

    list_of_unique_numbers = []

    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers


print(get_unique_numbers(numbers))

result: [1, 2, 3, 4, 5]


define a function, square the numbers in a range and append to a list.

li = [1, 2, 3, 4, 5]

def square_my_numbers(l):

    list_of_square_numbers = []

    for x in l:
        list_of_square_numbers.append(x ** 2)

    return list_of_square_numbers

print(square_my_numbers(li))



my_square = square(li)
print(my_square)

my_square2 = list(map(lambda x : x**2, li))
print(my_square2)
